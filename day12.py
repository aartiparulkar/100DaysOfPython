import random
logo = r"""
  /$$$$$$                                               /$$$$$$$$ /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                             |__  $$__/| $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/                                                                                                                                               
"""


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def guess_correct(user_guess, actual_number, turns):
    if user_guess < actual_number:
        print("Too low.")
        return turns - 1
    elif user_guess > actual_number:
        print("Too high.")
        return turns - 1
    else:
        print(f"You guessed {actual_number} right! 🤑🤑")
        

def choose_difficulty():
    level = input("Choose your difficulty. Type 'easy' or 'hard': ")
    return EASY_LEVEL_ATTEMPTS if level == 'easy' else HARD_LEVEL_ATTEMPTS
    

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 to 100.")
    number = random.randint(1, 100)
    # print(number)

    attempts_left = choose_difficulty()
    guess = 0
    while guess != number:
        print(f"You have {attempts_left} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        attempts_left = guess_correct(user_guess=guess, actual_number=number, turns=attempts_left)

        if attempts_left == 0:
            print("You've run out of guesses. 😭😭")
            return
        elif guess != number:
            print("Guess again")


while True:
    game()
    
    if input("Do you want to play again? Type 'y' to play, or 'n' otherwise: ") == 'n':
        break