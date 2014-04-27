'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert
@date: April 2014
'''

import sys
import os
import datetime

import Globals


def main():
    readInputFile()

def readInputFile():
    input_file = open(sys.argv[1], "r")
    lines = input_file.readlines()
    count = 0
    # Create a message object for each message
    for line in lines:
        date_raw = line[line.find("<date>") + 6:line.find("</date>")]
        year = date_raw[0:4]
        month = padMonth(date_raw)
        day = padDay(date_raw)
        
        time_raw = line[line.find("<time>") + 6:line.find("</time>")]
        first_colon = find_nth(time_raw,":",1)
        second_colon = find_nth(time_raw,":",2)
        third_colon = find_nth(time_raw,":",3)
    
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
        count += 1
                    
        # Create the DateTime object
        try:
            timestamp = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute),int(seconds),int(microseconds))
        # If malformed input, just throw out the data point
        except ValueError:
            continue
        
        if count % 500000 == 0:
            print(str(count) + "\t|" + str(timestamp))
        
        # Extract other components of message
        
        # Create new Message object, add it to global all_messages

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def padMonth(date_raw):
    first_dash = 5
    second_dash = date_raw[first_dash:].find("-") + first_dash
    month = date_raw[first_dash:second_dash]
    if len(month) == 1:
        return "0" + month
    else:
        return month

def padDay(date_raw):
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
