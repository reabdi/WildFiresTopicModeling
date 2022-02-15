import tweepy
import csv


# input your credentials here
# You need a Tweeter developer account to get these keys
# https://developer.twitter.com/en
consumer_key = '*************************'              
consumer_secret = '*************************'
access_token = '*************************'
access_token_secret = '*************************'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('YOUR_FILE_NAME.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)

# If you want to stream in general:
#for tweet in tweepy.Cursor(api.search, q="wildfire -filter:retweets",  count=1000000,
#                           lang="en",
#                           since="2020-09-23",
#                           until="2020-09-24"
#                           ).items():

# If you want to get the tweets of a specfic user:
for tweet in tweepy.Cursor(api.user_timeline, screen_name='@SenKamalaHarris',  count=1000000,
                           lang="en",
                           ).items():

    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at,tweet.user.id_str, tweet.user.screen_name, tweet.text.encode('utf-8'),
    tweet.retweet_count, tweet.favorite_count])
