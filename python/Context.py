'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert Haque
@date: April 2014
'''

from Enumerations import Button

class Context:
    # All eight buttons
    button_count = None
    # Total messages sent during this time quanta
    total_messages = 0
    # Number of spam (non-command) messages
    number_spam = 0
    # Timestamp at second resolution
    timestamp = None
    # Anarchy or democracy
    current_mode = None

    def __init__(self, timestamp):
        self.timestamp = timestamp
        # Instantiate our button counter
        self.button_count = dict()
        for button in Button:
            self.button_count[button] = 0
            
    def addMessageToContext(self, message):
        msg = message.lower()
        if msg is "up":
            self.button_count[Button.up] += 1
        elif msg is "down":
            self.button_count[Button.down] += 1
        elif msg is "left":
            self.button_count[Button.left] += 1
        elif msg is "right":
            self.button_count[Button.right] += 1
        elif msg is "a":
            self.button_count[Button.a] += 1
        elif msg is "b":
            self.button_count[Button.b] += 1
        elif msg is "start":
            self.button_count[Button.start] += 1
        elif msg is "select":
            self.button_count[Button.select] += 1
        else:
            self.number_spam += 1
        self.total_messages += 1
            