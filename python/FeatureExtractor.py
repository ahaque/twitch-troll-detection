'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert
@date: April 2014
'''

import sys
import os
from datetime import datetime, timedelta

import Globals
from User import User
from Context import Context
from Enumerations import Button, Mode

def main():
    '''
    print("Frequencies file column order")
    for button in Button:
        print(button)
    for mode in Mode:
        print(mode)
    print("total msg")
    print("spam freq")
    '''
    fe = FeatureExtractor()
    fe.readFrequencyFile()
    fe.extractFeatures()

    fe.output_file.close()
    fe.output_user_file.close()

class FeatureExtractor():
    context_history = None
    context_dict = None
    output_file = None
    output_user_file = None
    all_users = dict()
    
    def __init__(self):
        self.context_history = []
        self.output_file = open(sys.argv[3], "w")
        self.output_user_file = open(sys.argv[4], "w")
        self.context_dict = dict()
        
    def extractFeatures(self):
        # Read lines
        input_xml_file = open(sys.argv[1])
        lines = input_xml_file.readlines()
        context_index = 0
        current_context = self.context_history[context_index]
        line_count = 0
        for line in lines:
            line_timestamp = self.extractTimestamp(line)
            # Handles malformed timestamps
            if line_timestamp is None:
                continue
            
            # Do we need to update the context?
            if context_index+1 < len(self.context_history):
                if line_timestamp > self.context_history[context_index+1].timestamp:
                    current_context = self.context_history[context_index+1]
                    context_index += 1
            # Extract other components of message
            line_message = line[line.find("<msg>")+5:line.find("</msg>")]
            line_username = line[line.find("<user>")+6:line.find("</user>")]
            
            if line_username not in self.all_users.keys():
                u = User(line_username)
                u.processMessage(current_context, line_message)
                self.all_users[line_username] = u
            else:
                self.all_users[line_username].processMessage(current_context, line_message)
                
            line_count += 1
            if line_count % 1000000 == 0:
                print("Finished processing user messages: " + str(line_count))
        
        print("Number of unique users: " + str(len(self.all_users.keys())))
        print("Writing feature vectors to file...")
        for username in self.all_users.keys():
            self.output_user_file.write(username + "\n")
            fv = self.all_users[username].getFeatureVector()
            for i in range(0,len(fv)-1):
                self.output_file.write(str(fv[i]) + ",")
            self.output_file.write(str(fv[len(fv)-1])+"\n")
            
        print("Done! Terminating.")
            
    def readFrequencyFile(self):
        input_frequencies_file = open(sys.argv[2], "r")
        
        lines = input_frequencies_file.readlines()
        count = 0
        for line in lines:
            row = line.split(",")
            timestamp = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            c = Context(timestamp)
            button_freq_list = []
            mode_freq_list = []
            for i in range(1,9):
                button_freq_list.append(float(row[i]))
            mode_freq_list.append(float(row[9]))
            mode_freq_list.append(float(row[10]))

            c.populateFromFile(button_freq_list, mode_freq_list, int(row[11]), float(row[12]))
            self.context_history.append(c)
            
            count += 1
            if count % 10000 == 0:
                print("Finished Reading Frequency: " + str(count) + " / 270000")
    
    def calculateFrequenciesFromXML(self):
        input_file = open(sys.argv[1], "r")
        lines = input_file.readlines()
        
        num_lines_parsed = 0
        # Set up the first context
        current_context = Context(self.extractTimestamp(lines[0]))
        for line in lines:
            
            line_timestamp = self.extractTimestamp(line)
            # Handles malformed timestamps
            if line_timestamp is None:
                continue
            # Extract other components of message
            line_message = line[line.find("<msg>")+5:line.find("</msg>")]
                        
            # If we hit a new second, that is the two timestamps differ by more than the context duration
            if line_timestamp - current_context.timestamp > timedelta(seconds=Globals.CONTEXT_DURATION-1):
                self.writeContextToFile(current_context)
                self.context_history.append(current_context)
                current_context = Context(line_timestamp)
            # Else, we're in the same second, so update the current context
            else:
                current_context.addMessageToContext(line_message)

            
            num_lines_parsed += 1
            if num_lines_parsed % 1000000 == 0:
                print("Finished: " + str(num_lines_parsed))

        # Add the latest context
        self.context_history.append(current_context)
        self.writeContextToFile(current_context)
        self.output_file.close()
    
    def writeContextToFile(self, context):
        # timestamp, buttons,..., total_msg, percent spam
        self.output_file.write(str(context.timestamp)+",")
        button_freq = context.getButtonFrequencies()
        mode_freq = context.getModeFrequencies()
        for button in Button:
            self.output_file.write(str(button_freq[button]) + ",")
        for mode in Mode:
            self.output_file.write(str(mode_freq[mode]) + ",")
        self.output_file.write(str(context.total_messages) + "," + str(context.getSpamFrequency()) +"\n")
        
    '''
    Input: XML line from dataset
    Output: DateTime timestamp of message  
    '''       
    def extractTimestamp(self, line):
        date_raw = line[line.find("<date>") + 6:line.find("</date>")]
        year = date_raw[0:4]
        month = self.padMonth(date_raw)
        day = self.padDay(date_raw)
            
        time_raw = line[line.find("<time>") + 6:line.find("</time>")]
        first_colon = self.find_nth(time_raw,":",1)
        second_colon = self.find_nth(time_raw,":",2)
        third_colon = self.find_nth(time_raw,":",3)
    
        hour = time_raw[0:first_colon]
        minute = None
        seconds = None
        microseconds = None
        # Some data points are missing seconds
        if second_colon > 0:
            minute = time_raw[first_colon+1:second_colon]
            if third_colon > 0:
                seconds = time_raw[second_colon+1:third_colon]
            else:
                seconds = time_raw[second_colon+1:]
        else:
            minute = time_raw[first_colon+1:]
            seconds = "0"
        # Some data points are missing microseconds
        if third_colon > 0:
            microseconds = time_raw[third_colon+1:]
        else:
            microseconds = "0"
        
                    
        # Create the DateTime object
        try:
            #timestamp = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(seconds), int(microseconds))
            timestamp = datetime(int(year), int(month), int(day), int(hour), int(minute), int(seconds))
        # If malformed input, just throw out the data point
        except ValueError:
            return None
        
        return timestamp
    
    '''
    Input: string, substring, nth occurrence
    Output: Index of nth occurrence, -1 if doesn't exist
    '''
    def find_nth(self, haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start
    
    '''
    Input: content between <date> and </date>
    Output: Two digit month with leading zero
    '''
    def padMonth(self, date_raw):
        first_dash = 5
        second_dash = date_raw[first_dash:].find("-") + first_dash
        month = date_raw[first_dash:second_dash]
        if len(month) == 1:
            return "0" + month
        else:
            return month
        
    '''
    Input: content between <date> and </date>
    Output: Two digit day with leading zero
    '''
    def padDay(self, date_raw):
        first_dash = 5
        second_dash = date_raw[first_dash:].find("-") + first_dash
        day = date_raw[second_dash + 1:]
        if len(day) == 1:
            return "0" + day
        else:
            return day

if __name__ == '__main__':
    # Input parameter validation
    usage_message = "   USAGE: python3 FeatureExtractor.py <input xml file> <input frequencies file> <output feature file> <output user list>"  
    if len(sys.argv) != 5:
        print("   ERROR: You must supply all program arguments. You entered: " + str(len(sys.argv) - 1) + " arguments.")
        print(usage_message)
        sys.exit(0)
    if os.path.isfile(sys.argv[1]) is False:
        print("   ERROR: The input file \"" + sys.argv[1] + "\" does not exist.")
        print(usage_message)
        sys.exit(0)
    if os.path.isfile(sys.argv[2]) is False:
        print("   ERROR: The input file \"" + sys.argv[2] + "\" does not exist.")
        print(usage_message)
        sys.exit(0)
    main()
