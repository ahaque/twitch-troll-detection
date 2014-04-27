'''
Twitch Plays Pokemon, Machine Learns Twitch
@author: Albert Haque
@date: April 2014
'''

class Message(object):
    value = None
    timestamp = None
    username = None

    def __init__(self, username, timestamp, value):
        self.username = username
        self.timestamp = timestamp
        self.value = value