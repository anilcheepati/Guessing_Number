import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game !")
print("Think the number between 1 to 100 ")

level=input("choose a difficulty type:- easy or hard ").lower()




choose=random.randrange(1, 101)
print(f"Guessing number is : {choose}")

if level=="easy":
    easy_attempts=10
    print(f"You will have only {easy_attempts} guesses to win the game")
    while(easy_attempts!=0):
        easy_person_choice=int(input("Enter a number in between 1 to 100 :"))
        if choose!=easy_person_choice:
            easy_attempts-= 1
        else:
            print("You Won !")
            break
        if choose > easy_person_choice:
            print(f"Too low number: {easy_person_choice} and you have {easy_attempts} attempts left")
        else:
            print(f"Too high number : {easy_person_choice} and you have {easy_attempts} attempts left")

elif level=="hard":
    hard_attempts=5
    print(f"You will have only {hard_attempts} guesses to win the game")
    while(hard_attempts!=0):
        hard_person_choice=int(input("Enter a number in between 1 to 100 :"))
        if choose!=hard_person_choice:
            hard_attempts-= 1
        else:
            print("You Won !")
            break
        if choose > hard_person_choice:
            print(f"Too low number: {hard_person_choice} and you have {hard_attempts} attempts left")
        else:
            print(f"Too high number : {hard_person_choice} and you have {hard_attempts} attempts left")

else:
    print("Invalid difficulty level typed by User")











