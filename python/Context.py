'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert Haque
@date: April 2014
'''

from Enumerations import Button

class Context:
    # All eight buttons
    button_counts = None
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
        self.button_counts = dict()
        for button in Button:
            self.button_counts[button] = 0
            
    def getSpamFrequency(self):
        return self.number_spam/self.total_messages
    
    def getButtonFrequencies(self):
        frequencies = dict()
        # Get total button inputs
        total_button_inputs = sum(self.button_counts.values())
        # Calculate percentages
        for button in Button:
            frequencies[button] = self.button_counts[button]/total_button_inputs
        return frequencies
    
    def addMessageToContext(self, message):
        msg = message.lower()
        if msg == "up":
            self.button_counts[Button.up] += 1
        elif msg == "down":
            self.button_counts[Button.down] += 1
        elif msg == "left":
            self.button_counts[Button.left] += 1
        elif msg == "right":
            self.button_counts[Button.right] += 1
        elif msg == "a":
            self.button_counts[Button.a] += 1
        elif msg == "b":
            self.button_counts[Button.b] += 1
        elif msg == "start":
            self.button_counts[Button.start] += 1
        elif msg == "select":
            self.button_counts[Button.select] += 1
        else:
            self.number_spam += 1
        self.total_messages += 1
            