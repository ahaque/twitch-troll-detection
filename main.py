# Author: Albert Haque
# Date: April 2014
# Twitch Plays Pokemon, Machine Learns Twitch

import sys
import os
import numpy as np

class Context:
    def __init__(self):
        i = 0

def main():
    # Input error handling
    usage_message = "   USAGE: python main.py <dataset file>"  
    if len(sys.argv) != 2:
        print("   ERROR: You must supply all program arguments. You entered: " + str(len(sys.argv)-1) + " arguments.")
        print(usage_message)
        sys.exit(0)
    if os.path.isfile(sys.argv[1]) is False:
        print("   ERROR: The input file \"" + sys.argv[1] + "\" does not exist.")
        print(usage_message)
        sys.exit(0)

    input_file = open(sys.argv[1], "r")
    date_frequency = dict()

    lines = input_file.readlines()
    count = 0
    for line in lines:
        date_raw = line[line.find("<date>")+6:line.find("</date>")]
        # Convert 1 digit numbers to 2 digits
        year = date_raw[0:4]
        month = padMonth(date_raw)
        day = padDay(date_raw)
        formatted_date = year + "-" + month + "-" + day
        
        if formatted_date in date_frequency:
            date_frequency[formatted_date] += 1
        else:
            date_frequency[formatted_date] = 1
        count += 1
    
    for key in date_frequency.keys():
        print key + "\t" + str(date_frequency[key])
    print "Total Messages: " + str(count)

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
    day = date_raw[second_dash+1:]
    if len(day) == 1:
        return "0" + day
    else:
        return day

if  __name__ =='__main__':
    main()