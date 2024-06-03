# Rock - Paper - Scissors Game

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

print("\n Welcome to this amazing game! Have fun!\n")

game = [rock, paper, scissors]

game_len = len(game)

# user inputs choice

choice = int(input("Please choose 0 for rock, 1 for paper or 2 for scissors\n"))

if choice == 0:
    print(rock)
    
elif choice == 1:
    print(paper)
    
elif choice == 2:
    print(scissors)
    
else:
    print("Invalid Choice")
    
# Computer randomly selects

computer_choice_index = random.randint(0, game_len-1) # index of the randomly selected game item choice
computer_choice = game[computer_choice_index]
print(computer_choice)

# Game rules

# For a draw to happen
if computer_choice_index == choice:
    print("You draw!")

# This is rule #1, Rock wins against scissors    
if computer_choice_index == 0 and choice == 2:
    print("You lose")

elif computer_choice_index == 2 and choice == 0:
    print("You win")

# This is rule #2, Scissors win against paper    
if computer_choice_index ==2 and choice == 1:
    print("You lose")   
    
elif computer_choice_index ==1 and choice == 2:
    print("You win")

# This is rule #3, Paper wins against rock    
if computer_choice_index ==1 and choice == 0:
    print("You lose")
    
elif computer_choice_index ==0 and choice == 1:
    print("You win")
    
# an invalid entry
else:
    print("Your choice was invalid, you lose")
    
print("\n Thank You For Playing this game! Hope you had a blast!\n")
    