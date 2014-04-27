'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert
@date: April 2014
'''

import sys
import os
import datetime

from pprint import pprint
from Enumerations import Button

def main():
    fe = FeatureExtractor()
    #fe.readInputFile()
    fe.setupTrailingRecords()
    pprint(fe.trailing_inputs)

class FeatureExtractor():
    trailing_inputs = None
    trailing_total_messages = None
    trailing_spam = None
    
    def setupTrailingRecords(self):
        self.trailing_inputs = dict()
        for button in Button:
            self.trailing_inputs[button] = []
            
        self.trailing_total_messages =  []
        self.trailing_spam = []
    
    def readInputFile(self):
        input_file = open(sys.argv[1], "r")
        lines = input_file.readlines()
        
        num_lines_parsed = 0
        # Create a message object for each message
        for line in lines:
            
            timestamp = self.extractTimestamp(line)
            # Extract other components of message
            message = line[line.find("<msg>")+5:line.find("</msg>")]
            username = line[line.find("<user>")+6:line.find("</user>")]
            
            num_lines_parsed += 1
            if num_lines_parsed % 500000 == 0:
                print("Finished: " + str(num_lines_parsed))

    
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
            timestamp = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(seconds), int(microseconds))
        # If malformed input, just throw out the data point
        except ValueError:
            continue
        
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
