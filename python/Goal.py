'''
@author: Albert Haque
@date: April 2014

A Goal object consists of a specific button and the strength of the goal.
That is, how important is this goal compared to other concurrent goals.
'''

from Enumerations import Button

class Goal:
    # Must be of type Button
    button = None
    # Must be between 0 and 1
    strength = 0.0

    def __init__(self, button, strength):
        # Error handling
        if not self.isValidButton(button) or not self.isValidStrength(strength):
            return
        # Instantiate the Goal object
        self.button = button
        self.strength = strength
        
    def isValidButton(self, b):
        if not isinstance(b, Button):
            return False
        return True
    
    def isValidStrength(self, s):
        if type(s) is not float:
            return False
        # Strength is a percentage
        if s > 1.0 or s < 0.0:
            return False
        return True
    
    def reset(self):
        self.button = None
        self.strength = 0.0