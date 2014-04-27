'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert
@date: April 2014
'''

import sys
import os

from datetime import datetime, timedelta
from pprint import pprint

from Context import Context


def main():
    fe = FeatureExtractor()
    fe.readInputFile()

class FeatureExtractor():
    context_history = None
    
    def __init__(self):
        self.context_history = []
    
    def readInputFile(self):
        input_file = open(sys.argv[1], "r")
        lines = input_file.readlines()
        
        num_lines_parsed = 0
        # Set up the first context
        current_context = Context(self.extractTimestamp(lines[0]))
        for line in lines:
            
            line_timestamp = self.extractTimestamp(line)
            # Extract other components of message
            line_message = line[line.find("<msg>")+5:line.find("</msg>")]
            line_username = line[line.find("<user>")+6:line.find("</user>")]
                        
            # If we hit a new second, that is the two timestamps differ by more than 1 second
            if line_timestamp - current_context.timestamp > timedelta(seconds=1):
                print("DateTime: " + str(current_context.timestamp) + " | Total Msg=" + str(current_context.total_messages) + " | SPAM %: " + str(current_context.getSpamFrequency()))
                pprint(current_context.getButtonFrequencies())
                self.context_history.append(current_context)
                current_context = Context(line_timestamp)
            # Else, we're in the same second, so update the current context
            else:
                current_context.addMessageToContext(line_message)

            
            num_lines_parsed += 1
            if num_lines_parsed % 500000 == 0:
                print("Finished: " + str(num_lines_parsed))

        # Add the latest context
        self.context_history.append(current_context)
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
            pass
        
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
    usage_message = "   USAGE: python main.py <dataset file>"  
    if len(sys.argv) != 2:
        print("   ERROR: You must supply all program arguments. You entered: " + str(len(sys.argv) - 1) + " arguments.")
        print(usage_message)
        sys.exit(0)
    if os.path.isfile(sys.argv[1]) is False:
        print("   ERROR: The input file \"" + sys.argv[1] + "\" does not exist.")
        print(usage_message)
        sys.exit(0)
    main()
