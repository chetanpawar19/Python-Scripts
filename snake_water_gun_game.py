"""
Snake-water-gun computer:user game

Conditions-
water - gun = gun
water -snake = snake
water - water = drawn
snake - gun = gun
snake - snake = drawn
gun - gun = drawn
"""

from random import choice

choices = ["water","gun","snake"]
priority = {"water": 1,"snake":2,"gun":3}
no_of_chances = 5
computer_score = 0
user_score = 0
chances = 0

while True:
    computer_choice = choice(choices)
    user_choice = input("Enter your choice(gun,water,snake): ")
    if computer_choice == user_choice:
        continue
    else:
        if priority[computer_choice]>priority[user_choice]:
            computer_score+=1
            chances+=1
        else:
            user_score+=1
            chances += 1

    if no_of_chances == chances:
        break

if computer_score == user_score:
    print("it's tie game!")
elif computer_score>user_score:
    print("computer win the game, computer score is ",computer_score, "user score is ",user_score)
else:
    print("user win the game, computer score is ", computer_score, "user score is ", user_score)