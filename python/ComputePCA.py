'''
Twitch Plays Pokemon, Machine Learns Twitch

@author: Albert Haque
@date: April 2014
'''

import sys
import os

class PcaCalculator:

    input_file = None
    output_file = None
    feature_matrix = None

    def __init__(self):
        pass
    
    def readFeatureMatrix(self, input_filename):
        self.input_file = open(input_filename, "r")
        

def main():
    pca = PcaCalculator()
    pca.buildMatrix()
        
if __name__ == '__main__':
    # Input parameter validation
    usage_message = "   USAGE: python ComputePCA.py <input feature csv> <output pca>"  
    if len(sys.argv) != 3:
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