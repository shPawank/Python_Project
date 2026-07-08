#Snake Water Gun Game

import random

choices = ['snake', 'water', 'gun']
computer_choice = random.choice(choices)
print(computer_choice)

user=input("Enter your choice (snake, water, gun): ")
if user==computer_choice:
    print("It's a tie!")
elif(
    (user == "snake" and computer_choice == "water") or
    (user == "water" and computer_choice == "gun") or
    (user == "gun" and computer_choice == "snake")
):
    print("You win!")
else:
    print("Invalid input")