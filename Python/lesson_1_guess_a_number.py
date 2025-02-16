from random import randint

random_number = randint(1, 100)
attempt_counter = 0
user_input = int(input("Let's play the game! I'll guess the number, and you try to guess it, take a number from 1 to 100: "))

while True:
    attempt_counter += 1
    if 1 > user_input > 100:
        user_input = int(input("invalid number, please try again: "))
    elif user_input > random_number:
        if  user_input - random_number == 1:
            user_input = int(input("so close, try again: "))
        elif user_input - random_number < 10:
            user_input = int(input("very close, you need a smaller number, try again: "))
        else:
            user_input = int(input("Oh, that's too much, let's try again: "))
    elif user_input < random_number:
        if  random_number - user_input == 1:
            user_input = int(input("so close, try again: "))
        elif  random_number - user_input < 10:
            user_input = int(input("very close, you need a higher number, try again: "))
        else:
            user_input = int(input("Oh, that's too little, let's try again: "))
    else:
        print(f"You guessed right! The count of your attempts is: {attempt_counter}.")
        break



