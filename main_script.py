from collect_tweets import *


# Authenticate
twitter_auth_filename = sys.argv[1]
api = authenticate(twitter_auth_filename)
    

# get query of malware names and make a list out of it
name_query = sys.argv[2]
malware_names = []
f = open(name_query, "r")
for line in f.readlines():
    malware_names.append(line.strip())

    
# check for directory to store output file : storing in tweets folder
dir_name = "tweets"
if os.path.isdir(dir_name) is False:
    os.mkdir(dir_name)
print(f"**** Tweets stored in folder : {dir_name} ***")
directory = dir_name
    

# create a file with timestamp every time script runs
today = datetime.today()
today = str(today.year) + "-" + str(today.month) + "-" + str(today.day) +\
        "_at_" + str(today.hour) + "-" + str(today.minute)
file = '{}/output-{}.txt'.format(directory,today)

tweets_per_qry = 100
min_id = None   # None : fetch all tweets as much allowed.
max_id = -1     # -1 : start from the most recent one.
tweet_count = 0 # keep track of tweets fetched
stop = 1000000  # Stop when you collect this number of tweets.
    
for term in malware_names:
    print("---------------------")
    print('Search term =', term)
    
    query = term+" -filter:retweets"
    
    count = fetch_tweets(api, tweet_count, stop, min_id, max_id, tweets_per_qry, file, query)
    tweet_count += count
    
    if tweet_count >= stop:
        break

print("--------------------")
print (f"Downloaded {count} tweets, saved to {file}")

print("\n*** End of Script ***")
