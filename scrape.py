import random
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



handle = input('enter a twitter handle: ')
texty = get_tweets(handle)

#print(texty)

def text_skipper(text, current):
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
    
    return skip

def markov(stringer_return):
    words = texty.split()
    dict = {}
    current_word = '$'
    skipper = False

    for next_word in words:
        """ so far, the skipper function is not effective.
        Will revisit later."""
        skipper = text_skipper(next_word, skipper)
        if skipper:
            pass
        elif current_word not in dict:
            if current_word[-1] not in '!.?':
                dict[current_word] = [next_word]
        else:
            dict[current_word] += [next_word]
        
        if next_word[-1] in '!?.':
            current_word = '$'
        else:
            current_word = next_word
    
    return dict

dictionary = markov(texty)
print(dictionary)

def generate_text(word_dict, num_words):
    """ takes a dictionary and a positive integer num_words;
        uses word_dict to generate and print num_words words.
    """
    current_word = '$'
    increment = 0
    text = ''

    """considering using a while *increment* < num_words
    instead of a for loop so that I can end with punctuation.
    Then don't increment if *increment* == num_words - 1 and
    current_word[-1] != '.?!' """
    while increment < num_words:
        if current_word[-1] in '.?!':
            next_word = random.choice(word_dict['$'])
            #print(next_word, end=' ')
        else:
            next_word = random.choice(word_dict[current_word])
            #print(next_word, end=' ')
            if current_word != '$':
                text += current_word + ' '

        if next_word not in word_dict:
            current_word = '$'
        else:
            current_word = next_word
        increment += 1

        
    """ consider recursion for finishing a sentence with punctuation"""
    return text

tweet = generate_text(dictionary, 25)

#generate_text(dictionary, 20)
print(tweet)