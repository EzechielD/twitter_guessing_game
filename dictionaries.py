import tweepy

from keys import consumer_key, consumer_secret, access_token, access_secret
from scrape import auth, api, get_tweets
from set import markov

auth.set_access_token(access_token, access_secret)

def dict_maker(handle):
    text = get_tweets(handle)
    dictionary = markov(text)
    
    return dictionary

PhillyD = dict_maker('PhillyD')

print(PhillyD)