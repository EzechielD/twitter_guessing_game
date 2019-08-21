import random

from create import generate_text
from dictionaries import lil_nas_x, mark_hamill, playstation
from scrape import get_tweets

def launcher(number):
    assert type(number) == 1 or 2 or 3

    if number == 1:
        real = retrieve_tweet('LilNasX')
        fake = generate_text(lil_nas_x, 10)
        print(question(real, fake))
    elif number == 2:
        real = retrieve_tweet('HamillHimself')
        fake = generate_text(mark_hamill, 10)
        print(question(real, fake))
    elif number == 3:
        real = retrieve_tweet('PlayStation')
        fake = generate_text(playstation, 10)
        print(question(real, fake))

def retrieve_tweet(account):
    statuses = get_tweets(account)
    status_list = statuses.split('\n')
    randomizer = random.choice(status_list)

    return randomizer

def question(t1, t2):
        text = 'which one is real?' + '\n\n'
        text += t1 + '\n\n' + 'or' + '\n\n' + t2

        return text


print ('Welcome to Twitwit! please select an option below.')

print('1.) Lil Nas X' + '\n' + 
    '2.) Mark Hamill' + '\n' +
    '3.) PlayStation')

account = int(input('choice: '))

launcher(account)