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
\nimport pandas as pd
import tweepy
import datetime
import twitter
from textblob import TextBlob
import sys
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
import re

2. Then you need to convert json files into csv files using jsonTocsv.py, install the packages below
import json
import csv
from collections import Counter

3. You can use analysis.ipynb to make charts, install the packages below
import os
import pandas as pd
import numpy as np
import matplotlib
import math
import random
import time
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

4. Lastly, you can do baseline evaluation with baseline.ipynb, install the packages below
import pandas as pd
import numpy as np
import matplotlib
import math
import random
import time
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
