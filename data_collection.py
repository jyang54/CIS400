#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 04:03:33 2021

@author: phabby
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 03:59:58 2021

@author: phabby
"""

import datetime

import twitter
from textblob import TextBlob

import sys
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
import re


def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):
    # A nested helper function that handles common HTTPErrors. Return an updated
    # value for wait_period if the problem is a 500 level error. Block until the
    # rate limit is reset if it's a rate limiting issue (429 error). Returns None
    # for 401 and 404 errors, which requires special handling by the caller.
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):

        if wait_period > 3600:  # Seconds
            print('Too many retries. Quitting.', file=sys.stderr)
            raise e

        # See https://developer.twitter.com/en/docs/basics/response-codes
        # for common codes

        if e.e.code == 401:
            print('Encountered 401 Error (Not Authorized)', file=sys.stderr)
            return None
        elif e.e.code == 404:
            print('Encountered 404 Error (Not Found)', file=sys.stderr)
            return None
        elif e.e.code == 429:
            print('Encountered 429 Error (Rate Limit Exceeded)', file=sys.stderr)
            if sleep_when_rate_limited:
                print("Retrying in 15 minutes...ZzZ...", file=sys.stderr)
                sys.stderr.flush()
                time.sleep(60 * 15 + 5)
                print('...ZzZ...Awake now and trying again.', file=sys.stderr)
                return 2
            else:
                raise e  # Caller must handle the rate limiting issue
        elif e.e.code in (500, 502, 503, 504):
            print('Encountered {0} Error. Retrying in {1} seconds' \
                  .format(e.e.code, wait_period), file=sys.stderr)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e

    # End of nested helper function

    wait_period = 2
    error_count = 0

    while True:
        try:
            return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError as e:
            error_count = 0
            wait_period = handle_twitter_http_error(e, wait_period)
            if wait_period is None:
                return
        except URLError as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("URLError encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise
        except BadStatusLine as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("BadStatusLine encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise


def twitter_search(twitter_api, q, max_results=200, **kw):
    # See https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    # and https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
    # for details on advanced search criteria that may be useful for
    # keyword arguments

    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = twitter_api.search.tweets(q=q, count=100, **kw)

    statuses = search_results['statuses']

    # Iterate through batches of results by following the cursor until we
    # reach the desired number of results, keeping in mind that OAuth users
    # can "only" make 180 search queries per 15-minute interval. See
    # https://developer.twitter.com/en/docs/basics/rate-limits
    # for details. A reasonable number of results is ~1000, although
    # that number of results may not exist for all queries.

    # Enforce a reasonable limit
    max_results = min(1000, max_results)

    for _ in range(10):  # 10*100 = 1000
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e:  # No more results when next_results doesn't exist
            break

        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([kv.split('=')
                       for kv in next_results[1:].split("&")])

        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

        if len(statuses) > max_results:
            break

    return statuses

# pre-processing raw tweet
def clean_tweet(tweet):
    #tweet = re.sub(r'@[A-Za-z0-9_]+', '', tweet)
    #tweet = re.sub(r'#', '', tweet)
    #tweet = re.sub(r'RT : ', '', tweet)
    #tweet = re.sub(r'https?:\/\/[A-Za-z0-9\.\/]+', '', tweet)
    #return tweet
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# applying textblob to get a credit
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# get analysis from polarity
def getAnalysis(num):
    if num<0:
        return 'negative'
    elif num>0:
        return 'positive'
    else:
        return 'neutral'


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

import pandas as pd
import tweepy


if __name__ == '__main__':
    q = '"COVID-19 vaccine" OR Pfizer OR Moderna OR J&J vaccine OR Janssen' + "-filter:retweets"
    tweets = []

    CONSUMER_KEY = 'lqJRuPjOgQqzDkjoit18gk0wf'
    CONSUMER_SECRET = 'hk9GogPPf4ujwA0tkWHxbypXleH3vB6wP9DooQ2Smi1c0WXjSr'
    OAUTH_TOKEN = '1373343577812705281-OZujR7COGlSLsOUjbG80XxKd0Vo5rI'
    OAUTH_TOKEN_SECRET = 'OgqWCdB8sqA92aX1GRuVZFy9GKsQWMkAS3meZMAupPxq9'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    search_results = tweepy.Cursor(api.search, q=q, tweet_mode="extended", lang="en", until = '2021-04-29').items(10000)

    
    tweets = [[tweet.id, tweet.user.screen_name, tweet.user.id, tweet.favorite_count, tweet.retweet_count, str(datetime_from_utc_to_local(tweet.created_at)), clean_tweet(tweet.full_text), getPolarity(clean_tweet(tweet.full_text)), getAnalysis(getPolarity(clean_tweet(tweet.full_text)))] for tweet in search_results]
   # print(tweets)
    df = pd.DataFrame(data=tweets, columns=['tweet_id', 'username', 'user_id', 'favorite_count', 'retweet_count', 'created_time', 'full_text', 'polarity', 'analysis'])
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    with open ('0428-10000' +'.json','w',encoding = 'utf-8') as fp:
        json.dump(parsed,fp,ensure_ascii = False, indent=4, sort_keys=True)
    
    