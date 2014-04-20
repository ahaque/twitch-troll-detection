twitch-troll-detection
======================

Unsupervised machine learning methods to detect and classify anomalies in streaming data. We apply this to the viral event, TwitchPlaysPokemon, and attempt to identify trolls in a live IRC chat.


MapReduce
--------
The Hadoop program parses XML-like input we collected from the Twitch Plays Pokemon IRC chat room and groups all messages by user. This will allow us to build a profile for each user who participated.