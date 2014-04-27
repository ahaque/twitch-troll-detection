'''
@author: Albert Haque
@date: April 2014
'''

import Globals

from datetime import datetime

from Enumerations import Button

class Context:
    
    # All eight goals
    all_goals = []
    # Number of spam (non-command) posts over total messages, will use a sliding window
    percent_spam = 0.0
    # Total messages over a sliding window
    msg_per_second = 0.0
    # Timestamp at second resolution
    timestamp = None
    # Anarchy or democracy
    current_mode = None

    def __init__(self):
        for button in Button:
            print(button)