from data import data
import random
from art import *
from replit import clear

data_size = 0
for i in data:
    data_size += 1

print('Welcome in higher/lower game!')
print(logo)
def get_random_account():
    return random.choice(data)

def format_data(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f'{name}, {description}  from {country}'
def check_answer(guess, a_follower, b_followers):
    if a_follower>b_followers:
        return guess=='a'
    else:
        return guess=='b'
def rounds():
    rounds=int(input('How much rounds do you wanna play? '))
    return rounds

def game():
    rounds_=rounds()
    should_continue = True
    points = 0
    round = 1
    compare_1 = get_random_account()
    compare_2 = get_random_account()
    while should_continue:
        compare_1=compare_2
        compare_2=get_random_account()
        while compare_1==compare_2:
            compare_2=get_random_account()

        print(f'Round {round}.')
        print(f"Compare A: {format_data(compare_1)}.")
        print(vs)
        print(f"Compare B: {format_data(compare_2)}.")
        guess=input('Who has more followers? Type A or B: ').lower()
        a_follower_count=compare_1['follower_count']
        b_follower_count=compare_2['follower_count']
        is_correct=check_answer(guess,a_follower_count,b_follower_count)
        if  is_correct:
            points+=1
            round+=1
            print(f'You\'re right! Current score: {points}')
        else:
            print(f"Sorry, that's wrong. Current score: {points}")
            round+=1
        if round==rounds_:
            should_continue=False
            print(f' Your score is {points}')
    once_again=input('Wanna play again?(y/n) ').lower()
    if once_again=='y':
        clear()
        game()
    else:
        print('Goodbye!')

game()