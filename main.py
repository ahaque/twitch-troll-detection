# Author: Albert Haque
# Date: April 2014
# Twitch Plays Pokemon, Machine Learns Twitch

import sys, os

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
    # Load into memory
    lines = input_file.readlines()

if  __name__ =='__main__':
    main()