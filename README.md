# CIS400
CIS400 Team Project - COVID19 Vaccine Sentiment Analysis

Team members:
Chen Yang
Hang Zhao
Jintao Yang
Sioiok Wong

Overview

The repository contains three folders - code, data and figure.
In code folder, there are data_collection.py for collecting tweets, jsonTocsv.py to convert json file to csv format, analysis.ipynb for analysing data and making charts, baseline.ipynb for baseline evaluation.

In data folder, all the data are saved in json and csv format.

In figure folder, all the charts and pictures are saved in png format.

Installation

First download Python from https://www.python.org/downloads/.
Twitter data collection requires a twitter developer account which can be created on http://developer.twitter.com/.
Once the account is created, you can find the keys and token when you creat an app.
Put the keys you got in data_collection.py to use Twitter APIs.

1. First you need to collect data using data_collection.py, you need to install the packages below
import pandas as pd<br/>
import tweepy<br/>
import datetime<br/>
import twitter<br/>
from textblob import TextBlob<br/>
import sys<br/>
import time<br/>
from urllib.error import URLError<br/>
from http.client import BadStatusLine<br/>
import json<br/>
import re

2. Then you need to convert json files into csv files using jsonTocsv.py, install the packages below
import json<br/>
import csv<br/>
from collections import Counter

3. You can use analysis.ipynb to make charts, install the packages below
import os<br/>
import pandas as pd<br/>
import numpy as np<br/>
import matplotlib<br/>
import math<br/>
import random<br/>
import time<br/>
import datetime<br/>
import matplotlib.pyplot as plt<br/>
import seaborn as sns<br/>
from nltk.corpus import stopwords<br/>
from nltk.tokenize import word_tokenize<br/>
from collections import Counter

4. Lastly, you can do baseline evaluation with baseline.ipynb, install the packages below
import pandas as pd<br/>
import numpy as np<br/>
import matplotlib<br/>
import math<br/>
import random<br/>
import time<br/>
import datetime<br/>
import matplotlib.pyplot as plt<br/>
import seaborn as sns<br/>
import nltk<br/>
from sklearn.feature_extraction.text import CountVectorizer<br/>
from sklearn.feature_extraction.text import TfidfVectorizer<br/>
from sklearn.model_selection import train_test_split<br/>
from sklearn.linear_model import LogisticRegression<br/>
from sklearn.ensemble import RandomForestClassifier<br/><br/>
from sklearn.svm import LinearSVC<br/>
from sklearn.naive_bayes import MultinomialNB<br/>
from sklearn.metrics import classification_report<br/>
from sklearn.neural_network import MLPClassifier
