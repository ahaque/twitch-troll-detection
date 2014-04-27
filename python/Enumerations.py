'''
@author: Albert Haque
@date: April 2014

Each of the following classes are enumerations used in our algorithm.
'''

from enum import Enum

class Button(Enum):
    up, down, left, right, a, b, start, select = range(8)
    
class Mode(Enum):
    anarchy, democracy = range(2)
    
class Label(Enum):
    troll, non_troll = range(2)