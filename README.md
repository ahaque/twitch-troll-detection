Twitch Plays Pokemon, Machine Learns Twitch
--------

[![arXiv](https://img.shields.io/badge/arXiv-1902.06208-b31b1b.svg)](https://arxiv.org/abs/1902.06208)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3932957.svg)](https://doi.org/10.5281/zenodo.3932957)

The dataset, titled the Twitch Plays Pokemon Dataset (TPP), contains 37.8 million IRC chat messages. It contains IRC chat log data for messages made between February 2, 2014 and April 23, 2014 (68 days). Each line denotes a single IRC chat message.

:point_right: Download link: [https://zenodo.org/record/3932957](https://zenodo.org/record/3932957) (534 MB compressed, 3.4 GB uncompressed)

Sample of the dataset:
```
<date>2014-02-14</date><time>08:17:32</time><user>medicblue</user><msg>a</msg>
<date>2014-02-14</date><time>08:17:32</time><user>murderousburger</user><msg>rare candy, RARE CANDY</msg>
<date>2014-02-14</date><time>08:17:32</time><user>milk2978</user><msg>B</msg>
<date>2014-02-14</date><time>08:17:32</time><user>mrtiktalik</user><msg>b</msg>
<date>2014-02-14</date><time>08:17:32</time><user>dualhammers</user><msg>b</msg>
<date>2014-02-14</date><time>08:17:32</time><user>shares5</user><msg>YES</msg>
<date>2014-02-14</date><time>08:17:32</time><user>orangerust</user><msg>start</msg>
<date>2014-02-14</date><time>08:17:32</time><user>snowiee</user><msg>a</msg>
<date>2014-02-14</date><time>08:17:33</time><user>duroate</user><msg>down</msg>
<date>2014-02-14</date><time>08:17:33</time><user>crypticcraig</user><msg>up</msg>
<date>2014-02-14</date><time>08:17:33</time><user>doug2725</user><msg>LOL HELIX FOSSIL WENT BACK THAT FAR</msg>
```

## Overview
Unsupervised machine learning methods to detect and classify anomalies in streaming data. We apply this to the viral event, TwitchPlaysPokemon, and attempt to identify trolls in a live IRC chat. For more information about what Twitch Plays Pokmeon, please see the Wikipedia article: http://en.wikipedia.org/wiki/Twitch_Plays_Pok%C3%A9mon

We use Java 7 and Python 3.4.0 in this repository. NumPy 1.8.1 and SciPy 1.8.1 were used in conjunction with Python 2.7.6.

## Abstract
With the increasing importance of online communities, discussion forums, and customer reviews, Internet “trolls” have proliferated thereby making it difficult for information seekers to find relevant and correct information. In this paper, we consider the problem of detecting and identifying Internet trolls, almost all of which are human agents. Identifying a human agent among a human population presents significant challenges compared to detecting automated spam or computerized robots. To learn a troll’s behavior, we use contextual anomaly detection to profile each chat user. Using clustering and distance-based methods, we use contextual data such as the group’s current goal, the current time, and the username to classify each point as an anomaly. A user whose features significantly differ from the norm will be classified as a troll. We collected 38 million data points from the viral Internet fad, Twitch Plays Pokemon. Using clustering and distance-based methods, we develop heuristics for identifying trolls. Using MapReduce techniques for preprocessing and user profiling, we are able to classify trolls based on 10 features extracted from a user’s lifetime history.

You can view the full technical paper here: [https://arxiv.org/abs/1902.06208](https://arxiv.org/abs/1902.06208)

## MapReduce
The Hadoop 2.2.0 program parses XML-like input we collected from the Twitch Plays Pokemon IRC chat room and groups all messages by user. This will allow us to build a profile for each user who participated. Because the file is several gigabytes in size, running MapReduce may be faster on some systems than a sequential program.

## Python
This folder is the bulk of the unsupervised algorithm. It contains all necessary classes: Context, Message, User, etc. To import this project into eclipse, you must have PyDev installed.

## Matlab
MATLAB code for clustering and distance calculations. This is compatible with Octave.

## Other
If you wish to cite this dataset or paper:

Haque, A. Twitch Plays Pokemon, Machine Learns Twitch: Unsupervised Context-Aware Anomaly Detection for Identifying Trolls in Streaming Data. University of Texas at Austin. 2014.

BibTeX
```
@article{haque2014twitch,
  title={Twitch Plays Pokemon, Machine Learns Twitch},
  author={Haque, Albert},
  institution={University of Texas at Austin},
  year={2014}
}
```
