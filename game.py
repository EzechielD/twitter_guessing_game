import random

from create import generate_text
from dictionaries import lil_nas_x, mark_hamill, playstation
from scrape import get_tweets

def launcher(number):
    assert type(number) == 1 or 2 or 3

    if number == 1:
        real = retrieve_tweet('LilNasX')
        fake = generate_text(lil_nas_x, 20)
        return(question(real, fake))
    elif number == 2:
        real = retrieve_tweet('HamillHimself')
        fake = generate_text(mark_hamill, 20)
        return(question(real, fake))
    elif number == 3:
        real = retrieve_tweet('PlayStation')
        fake = generate_text(playstation, 20)
        return(question(real, fake))

def retrieve_tweet(account):
    statuses = get_tweets(account)
    status_list = statuses.split('\n')  #working on an alternative split
    randomizer = random.choice(status_list)

    return randomizer

def question(tweet1, tweet2):
    options = [tweet1, tweet2]
    choice1 = random.choice(options)

    if choice1 == tweet1:
        choice2 = tweet2
        ans_one = True
    else:
        choice2 = tweet1
        ans_one = False
    
    text = 'which one is real?' + '\n\n'
    text += choice1 + '\n\n' + 'or' + '\n\n' + choice2 + '\n'

    print(text)

    num_answer = int(input('Type your answer here: '))

    check = score_state(num_answer, ans_one)

    return check

def score_state(num_answer, ans_one):
    assert num_answer == 1 or 2

    if num_answer == 1:
        if ans_one == True:
            correct = True
        else:
            correct = False
    else:
        if ans_one == True:
            correct = False
        else:
            correct = True
    
    if correct == True:
        print('Correct! choice ' + str(num_answer) + ' is real!')

    else:
        print('Incorrect!: choice ' + str(num_answer) + ' is fake!')
    
    return correct
        

answer = None

def game():
    #score = 0
    lives = 2
    check = None
    print('Welcome to Twitwit! Please select an option below.')

    print('1.) Lil Nas X' + '\n' + 
        '2.) Mark Hamill' + '\n' +
        '3.) PlayStation')

    account = int(input('choice: '))


    while lives > 0:
        print('loading...')
        check = launcher(account)
        if check == False:
            lives -= 1
            print('lives left: ' + lives)


game()