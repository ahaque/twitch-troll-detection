'''
@author: Albert Haque
@date: April 2014
Global variables for Machine Learns Twitch
'''

def init():
    # Use the past TRAILING_WINDOW for profile/context calculations
    global TRAILING_WINDOW
    TRAILING_WINDOW = 30
    
    global all_messages
    all_messages = []