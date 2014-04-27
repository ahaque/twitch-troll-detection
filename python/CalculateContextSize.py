'''
Created on Apr 27, 2014

@author: Albert
'''

import sys, os

def main():
    input_file = open(sys.argv[1], "r")
    
    lines = input_file.readlines()
    histogram = dict()
    for line in lines:
        msg_count = int(line.split(",")[11])
        bucket = round(msg_count, -1)
        if bucket in histogram.keys():
            histogram[bucket] += 1
        else:
            histogram[bucket] = 1
    
    output_file = open(sys.argv[2], "w")
    
    for bucket in histogram.keys():
        output_file.write(str(bucket) + "\t" + str(histogram[bucket]) + "\n")
    
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    # Input parameter validation
    usage_message = "   USAGE: python3 CalculateContextSize.py <input csv file> <output frequency file>"  
    if len(sys.argv) != 3:
        print("   ERROR: You must supply all program arguments. You entered: " + str(len(sys.argv) - 1) + " arguments.")
        print(usage_message)
        sys.exit(0)
    if os.path.isfile(sys.argv[1]) is False:
        print("   ERROR: The input file \"" + sys.argv[1] + "\" does not exist.")
        print(usage_message)
        sys.exit(0)
    main()