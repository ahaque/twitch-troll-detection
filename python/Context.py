'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert Haque
@date: April 2014
'''

from Enumerations import Button, Mode

class Context:
    # All eight buttons
    button_counts = None
    # Total messages sent during this time quanta
    total_messages = 0
    # Number of spam (non-command) messages
    number_spam = 0
    # Timestamp at second resolution
    timestamp = None
    # Counts of both modes
    mode_counts = None
    # Anarchy or democracy
    current_mode = None
    button_frequencies = None
    mode_frequencies = None
    percent_spam = None

    def __init__(self, timestamp):
        self.timestamp = timestamp
        # Instantiate our button counter
        self.button_counts = dict()
        for button in Button:
            self.button_counts[button] = 0
        # Instantiate the mode counter
        self.mode_counts = dict()
        for mode in Mode:
            self.mode_counts[mode] = 0
            
    def populateFromFile(self, button_freq_list, mode_freq, total_msg, spam):
        self.button_frequencies = dict()
        self.mode_frequencies = dict()
        i = 0
        for button in Button:
            self.button_frequencies[button] = button_freq_list[i]
            i += 1
        self.mode_frequencies[Mode.anarchy] = mode_freq[0]
        self.mode_frequencies[Mode.democracy] = mode_freq[1]
        self.total_messages = total_msg
        self.percent_spam = spam
        
            
    def getModeFrequencies(self):
        frequencies = dict()
        total_mode_inputs = sum(self.mode_counts.values())
        
        if total_mode_inputs == 0:
            for mode in Mode:
                frequencies[mode] = 0.0
            return frequencies
        
        for mode in Mode:
            frequencies[mode] = self.mode_counts[mode]/total_mode_inputs
        return frequencies
            
    def getSpamFrequency(self):
        if self.total_messages == 0:
            return 0.0
        else:
            return self.number_spam/self.total_messages
    
    def getButtonFrequencies(self):
        frequencies = dict()
        # Get total button inputs
        total_button_inputs = sum(self.button_counts.values())
        # If no button inputs, return all zeros
        if total_button_inputs == 0:
            for button in Button:
                frequencies[button] = 0.0
            return frequencies
        # Else, calculate percentages
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
        elif msg == "anarchy":
            self.mode_counts[Mode.anarchy] += 1
        elif msg == "democracy":
            self.mode_counts[Mode.democracy] += 1
        else:
            self.number_spam += 1
        self.total_messages += 1
            