from random import randint

def choose_game():
    attempt_counter = 0
    max_range = int(input("Let's play the game! I'll guess the number, and you try to guess it. Choose, how big our range is: "))
    user_input = int(input(f"Now, take a number from 1 to {max_range}: "))
    random_number = randint(1, max_range)
    while True:
        if 1 > user_input or user_input > max_range:
            user_input = int(input(f"invalid number, please enter a number from 1 to {max_range}: "))
            continue
            
        attempt_counter += 1
        if user_input > random_number:
            if  user_input - random_number == 1:
                user_input = int(input(f"#{attempt_counter} So close, enter a number: "))
            elif user_input - random_number < 10:
                user_input = int(input(f"#{attempt_counter} Very close, you need a smaller number, enter a number: "))
            else:
                user_input = int(input(f"#{attempt_counter} Oh, that's too much, let's enter a number: "))
        elif user_input < random_number:
            if  random_number - user_input == 1:
                user_input = int(input(f"#{attempt_counter} So close, enter a number: "))
            elif  random_number - user_input < 10:
                user_input = int(input(f"#{attempt_counter} Very close, you need a higher number, enter a number: "))
            else:
                user_input = int(input(f"#{attempt_counter} Oh, that's too little, let's enter a number: "))
        else:
            print(f"You guessed right! The count of your attempts is: {attempt_counter}.")
            return

while True:
    choose_game()
    if input('Do you want to repeat? (y/n) ').lower() != 'y':
        break
print('Game over')



