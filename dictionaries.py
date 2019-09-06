import tweepy

from keys import consumer_key, consumer_secret, access_token, access_secret
from scrape import auth, api, get_tweets
from create import markov, dict_maker

auth.set_access_token(access_token, access_secret)

#Dictionaries for specific accounts are created here
playstation = dict_maker("PlayStation")
lil_nas_x = dict_maker("LilNasX")
mark_hamill = dict_maker("HamillHimself")