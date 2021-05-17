# CIS400
CIS400 Team Project - COVID19 Vaccine Sentiment Analysis

Team members:
Chen Yang
Hang Zhao
Jintao Yang
Sioiok Wong

1. First you need to collect data using data_collection.py, you need to install the packages below
import pandas as pd
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
