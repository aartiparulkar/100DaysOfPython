from game_data import data
from art import logo, vs
from random import choice


def frame_question(option1, option2):
    print(f"Compare A: {option1['name']}, {option1['description']}, from {option1['country']}")
    print(vs)
    print(f"Against B: {option2['name']}, {option2['description']}, from {option2['country']}")


def is_correct(option1, option2, user_guess):
    if user_guess == 'a':
        return option1['follower_count'] > option2['follower_count']
            
    return option2['follower_count'] > option1['follower_count']


print(logo)

# Randomly pick 2 celebs/things/whatever it is
optionA, optionB = choice(data), choice(data)
current_score = 0
    
while True:    
    while optionA == optionB:
        optionB = choice(data)
    
    frame_question(optionA, optionB)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if is_correct(option1=optionA, option2=optionB, user_guess=guess):
        current_score += 1
        print(f"You're right! Your current score is {current_score}")
        print("\n"*20)
        
    else:
        print("\n"*20)
        print(f"Sorry that is wrong. Your final score is {current_score}")
        break

    optionA = optionB
    optionB = choice(data)
