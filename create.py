import random
import tweepy

from keys import consumer_key, consumer_secret, access_token, access_secret
from scrape import auth, api, get_tweets

auth.set_access_token(access_token, access_secret)


"""def text_skipper(text, current):
    retweet_check = 'RT'
    reply_check = '@'
    skip = current

    if skip:
        skip = False
    elif text[:2] == retweet_check:
        skip = True
    elif text[0] == reply_check:
        skip = True
    elif 'https://' in text:
        skip = True
    
    return skip"""

def markov(tweets):
    """ takes in the retrieved tweets from get_tweets;
    creates a dictionary of all of the words used in that
    account's last 200 tweets using a markov model
    """
    words = tweets.split()
    account_dict = {}
    current_word = '$'
    #skipper = False

    for next_word in words:
        "so far, the skipper function is not effective. May revisit later"
        #skipper = text_skipper(next_word, skipper)
        #if skipper == True:
        #    pass
        if current_word not in account_dict:
            if current_word[-1] not in '!.?':
                account_dict[current_word] = [next_word]
        else:
            account_dict[current_word] += [next_word]
        
        if next_word[-1] in '!?.':
            current_word = '$'
        else:
            current_word = next_word
    
    return account_dict

def generate_text(word_dict, num_words):
    """ takes a dictionary and a positive integer (num_words);
        uses word_dict to generate and print num_words words.
    """
    current_word = '$'
    increment = 0
    text = ''

    while increment < num_words:
        if current_word[-1] in '.?!':
            next_word = random.choice(word_dict['$'])
        else:
            next_word = random.choice(word_dict[current_word])
            if next_word != '$':
                text += next_word + ' '

        if next_word not in word_dict:
            current_word = '$'
        else:
            current_word = next_word
        increment += 1

    "consider recursion for finishing a sentence with punctuation"
    return text

def dict_maker(handle):
    """Takes in a twitter account name (handle);
    creates and returns the markov model dictionary
    """
    text = get_tweets(handle)
    dictionary = markov(text)
    
    return dictionary