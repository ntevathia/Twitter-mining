import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import dateutil.parser

def tweets_features(filename):
    '''
    Extract relevant tweet information from the json file passed as input.
    '''
    content = open(filename, "r")
    tweets_list = []
    for line in content:
        tweet = json.loads(line)
        
        tweet_dict = {}
        tweet_dict['id'] = tweet["id"]
        tweet_dict['text'] = tweet["text"]
        tweet_dict['user'] = tweet["user"]["screen_name"]
        tweet_dict['created'] = dateutil.parser.parse(tweet["created_at"])
        tweet_dict['retweeted'] = tweet["retweet_count"]
        tweet_dict['favorited'] = tweet["favorite_count"]
        tweet_dict['hashtags'] = tweet["entities"]['hashtags']
        tweet_dict['urls'] = tweet["entities"]['urls']
        tweet_dict['language'] = tweet["lang"]
        tweet_dict['coordinates'] = tweet["coordinates"]
        tweet_dict['geo'] = tweet["geo"]
        tweet_dict['place'] = tweet["place"]
        
        tweets_list.append(tweet_dict)
    content.close()
    
    return tweets_list

def tweets_to_df(directory):
    '''
    This function takes the path of all tweets file and returns the unique tweets 
    combined as a dataframe after removing the duplicate tweets.
    '''
    files = list(map(lambda x: directory+'/'+x, os.listdir(directory)))
    tweets = []
    for file in files:
        data = tweets_features(file)
        for line in data:
            tweets.append(line)

    tweets = pd.DataFrame(tweets)
    tweets = tweets.drop_duplicates(subset=['id'])
    
    return tweets

def viz_most_frequent_words(df_tweets):
    '''
    This function plots the word cloud with most frequent words from 
    column text.
    '''
    words = df_tweets.text.str.cat(sep=' ')
    wordcloud = WordCloud(width=1600, height=800, max_font_size=200).generate(words)
    plt.figure(figsize=(15,10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("tweets containing malware related common words", size=20)
    plt.show()
