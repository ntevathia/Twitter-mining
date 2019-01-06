# Twitter-mining

This repository is focusing on fetching tweets based on the key terms mentioned in a text file. Here I am trying to find all the tweets for malware names ( mentioned in malware_names.txt ). 

We can achieve so by using Twitter APIs available at Twitter Developers account  https://developer.twitter.com/en/docs/tweets/search/overview

Limitations of Twitter APIs: We get access to only past 7 days of data and could not fetch data past a week.

Work around : We can setup a cron job which runs every week to to get all the data.

How to run the script:
Use terminal and run the command `python main_script.py api_key.csv malware_names.txt`

api_key.csv - This file will have all the access and secret key to be used for twitter APIs.
malware_names.txt - File with key words for which tweets need to be fetched.
main_script.py - This script internally uses functions from collect_tweets.py where we are authenticating the API,
                 fetching the tweets based on the query
                 main_script.py will do all other tasks like creating the folder `tweet` to store the output for each run.
read_twitter.py - Here we are defining functions which select the relevant columns from each tweet and combine the data 
                  into a dataframe after removing duplicates to allow for easier access to data. Defined a function to do
                  wordcloud visualizations as well.


Future Work :
Visuals_WordCloud.ipynb - Some visuals of the tweets.
Cron_job.txt - Instructions of how to setup a crontab job to run weekly once.



