# Twitter-mining

This repository is focusing on fetching tweets based on the key terms mentioned in a text file. In my case I am trying to find all the tweets for malware names ( mentioned in malware_names.txt ). 

We can achieve so by using Twitter APIs available @https://developer.twitter.com/en/docs/tweets/search/overview [ Twitter Developers account ]

Limitations of Twitter APIs: We get access to only past 7 days of data and could not fetch data past a week.
Work around : We can setup a cron job which runs every week to to get all the data.



