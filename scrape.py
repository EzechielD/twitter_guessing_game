import tweepy

from keys import consumer_key, consumer_secret, access_token, access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def get_tweets(twitter_name):
    text = ''
    for tweet in tweepy.Cursor(api.user_timeline, id=twitter_name, tweet_mode="extended").items(200):
        text += tweet.full_text + '\n'


    return text
