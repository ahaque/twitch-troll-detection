Twitch Plays Pokemon, Machine Learns Twitch
--------

Unsupervised machine learning methods to detect and classify anomalies in streaming data. We apply this to the viral event, TwitchPlaysPokemon, and attempt to identify trolls in a live IRC chat.

We use Java 7 and Python 3.4.0 in this repository. NumPy 1.8.1 and SciPy 1.8.1 were used in conjunction with Python 2.7.6.

We made the dataset we collected publicly available. It is 561 MB compressed and 3.4 GB as an uncompressed XML-like file:
http://albert.cm/dl/tpp_data.zip

Here is how the dataset looks like:
```
	<date>2014-02-14</date><time>08:17:32</time><user>medicblue</user><msg>a</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>murderousburger</user><msg>rare candy, RARE CANDY</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>milk2978</user><msg>B</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>mrtiktalik</user><msg>b</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>holabio</user><msg>a</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>sama102</user><msg> b</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>dualhammers</user><msg>b</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>shares5</user><msg>YES</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>orangerust</user><msg>start</msg>
	<date>2014-02-14</date><time>08:17:32</time><user>snowiee</user><msg>a</msg>
	<date>2014-02-14</date><time>08:17:33</time><user>duroate</user><msg>down</msg>
	<date>2014-02-14</date><time>08:17:33</time><user>crypticcraig</user><msg>up</msg>
	<date>2014-02-14</date><time>08:17:33</time><user>doug2725</user><msg>LOL HELIX FOSSIL WENT BACK THAT FAR</msg>
```

mapreduce
--------
The Hadoop 2.2.0 program parses XML-like input we collected from the Twitch Plays Pokemon IRC chat room and groups all messages by user. This will allow us to build a profile for each user who participated.

python
--------
This project is the bulk of the unsupervised algorithm. It contains all necessary classes: Context, Message, User, etc. To import this project into eclipse, you must have PyDev installed.

matlab
--------
MATLAB code for clustering and distance calculations. This is compatible with Octave.


Citations
--------
If you wish to cite this dataset or paper:

Haque, A. Twitch Plays Pokemon, Machine Learns Twitch: Unsupervised Context-Aware Anomaly Detection for Identifying Trolls in Streaming Data. 2014.

BibTeX
```
@article{haque2014twitch,
  title={Twitch Plays Pokemon, Machine Learns Twitch: Unsupervised Context-Aware Anomaly Detection for Identifying Trolls in Streaming Data},
  author={Haque, Albert},
  year={2014}
}
```