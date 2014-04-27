twitch-troll-detection
======================

Unsupervised machine learning methods to detect and classify anomalies in streaming data. We apply this to the viral event, TwitchPlaysPokemon, and attempt to identify trolls in a live IRC chat.

We use Java 7 and Python 3.4.0 in this repository.

mapreduce
--------
The Hadoop 2.2.0 program parses XML-like input we collected from the Twitch Plays Pokemon IRC chat room and groups all messages by user. This will allow us to build a profile for each user who participated.

python
--------
This project is the bulk of the unsupervised algorithm. It contains all necessary classes: Context, Message, User, etc. To import this project into eclipse, you must have PyDev installed.