'''
Twitch Plays Pokemon, Machine Learns Twitch

@author: Albert Haque
@date: April 2014
'''

import sys
import os
import numpy
import scipy

class PcaCalculator:

    input_file = None
    output_file = None
    feature_matrix = None

    def __init__(self):
        pass
    
    def readFeatureMatrix(self, input_filename): 
        self.input_file = open(input_filename, "r")
        lines = self.input_file.readlines()
        count = 0
        float_matrix = []
        for line in lines:
            row = line.rstrip("\n").split(",")
            float_array = [float(i) for i in row]
            # Remove the first column which is the total messages sent
            # It was mainly used for debugging
            if float(row[0]) < 20:
                continue
            float_array.remove(float(row[0]))
            float_matrix.append(float_array)
            count += 1
            if count >= 15000:
                break
            
        self.feature_matrix = numpy.matrix(float_matrix)


    def calculateSVD(self):
        print "Calculating SVD..."
        U, s, Vh = numpy.linalg.svd(self.feature_matrix)
        print "Finished calculating SVD. Writing to files.."

def main():
    pca = PcaCalculator()
    pca.readFeatureMatrix(sys.argv[1])
    pca.calculateSVD()
    pca.writeSVDtoFile()
        
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
    main()
