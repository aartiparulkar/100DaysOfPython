import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
user_pick = int(input("What do you choose? Enter 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(choices[user_pick])

computer_pick = random.randint(0, 2)
print("\nComputer chose: ")
print(choices[computer_pick])

if user_pick == computer_pick:
    print("You draw!")
elif user_pick == 0:
    if computer_pick == 1:
        print("You lose.")
    else:
        print("You win!")
elif user_pick == 1:
    if computer_pick == 0:
        print("You lose.")
    else:
        print("You win!")
else:
    print("You entered an invalid number. You lose.")
