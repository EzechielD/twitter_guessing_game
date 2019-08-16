import random
import tweepy

from keys import consumer_key, consumer_secret, access_token, access_secret
from scrape import auth, api, get_tweets

auth.set_access_token(access_token, access_secret)

#handle = input('enter a twitter handle: ')
#tweets = get_tweets(handle)

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
    words = tweets.split()
    dict = {}
    current_word = '$'
    #skipper = False

    for next_word in words:
        " so far, the skipper function is not effective. Will revisit later."
        #skipper = text_skipper(next_word, skipper)
        #if skipper:
        #    pass
        if current_word not in dict:
            if current_word[-1] not in '!.?':
                dict[current_word] = [next_word]
        else:
            dict[current_word] += [next_word]
        
        if next_word[-1] in '!?.':
            current_word = '$'
        else:
            current_word = next_word
    
    return dict

#dictionary = markov(tweets)
#print(dictionary)

def generate_text(word_dict, num_words):
    """ takes a dictionary and a positive integer num_words;
        uses word_dict to generate and print num_words words.
    """
    current_word = '$'
    increment = 0
    text = ''


    while increment < num_words:
        if current_word[-1] in '.?!':
            next_word = random.choice(word_dict['$'])
            #print(next_word, end=' ')
        else:
            next_word = random.choice(word_dict[current_word])
            #print(next_word, end=' ')
            if next_word != '$':
                text += next_word + ' '

        if next_word not in word_dict:
            current_word = '$'
        else:
            current_word = next_word
        increment += 1

    "consider recursion for finishing a sentence with punctuation"
    return text

#tweet = generate_text(dictionary, 25)

#generate_text(dictionary, 20)
#print(tweet)

def dict_maker(handle):
    text = get_tweets(handle)
    dictionary = markov(text)
    
    return dictionary