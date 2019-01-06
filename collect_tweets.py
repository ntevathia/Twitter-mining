import tweepy
import os
import sys
import json
from datetime import datetime

def loadkeys(filename):
    '''
    Input is csv file with Twitter API authentication.
    Output is a list of tokens containing API key and secret key,
    access token key and access token secret key.
    '''
    with open(filename) as f:
        items = f.readline().strip().split(', ')
        return items

def authenticate(filename):
    '''
    Authenticates the key on twitter.
    '''
    keys = loadkeys(filename)
    
    consumer_key = keys[0]
    consumer_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)
    
    return api

def fetch_tweets(api, tweet_count, stop, min_id, max_id, tweets_per_qry, file, query):
    '''
    Tweets fetched for query will be appended to the file and the fetching limit per 
    iteration is tweets_per_qry. The function stops fetching once the tweet_count 
    reaches stop limit. min_id tells the latest tweet id from which the fetch starts 
    and max_id tells the oldest tweet fetched based on tweet_id. max_id and min_id 
    guides the fetching process. For every iteration we update max_id to the oldest 
    tweet_id to keep track of fetch of tweets.
    '''
    with open(file,'a') as f:
        while tweet_count<stop: 
        
            if (max_id <= 0):
                if (not min_id):
                    new_tweets = api.search(q=query, count=tweets_per_qry)
                else:
                    new_tweets = api.search(q=query, count=tweets_per_qry,
                                        since_id=min_id)
            else:
                if (not min_id):
                    new_tweets = api.search(q=query, count=tweets_per_qry,
                                        max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=query, count=tweets_per_qry,
                                        max_id=str(max_id - 1),
                                        since_id=min_id)

            # If query returns empty
            if not new_tweets:
                print("No more tweets found")
                break

            # Save to file
            for tweet in new_tweets:
                json.dump(tweet._json, f)
                f.write('\n')

            # track of tweet count    
            tweet_count += len(new_tweets)
            print(f"Downloaded {tweet_count} tweets")
        
            # Search tweets older than the last one collected.
            max_id = new_tweets[-1].id
    
    return tweet_count
