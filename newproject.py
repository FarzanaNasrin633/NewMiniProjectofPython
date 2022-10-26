from curses.ascii import isdigit
import random

count = 0
player_want_to_play = True

while True:
    input_number = input("Type a number: ")
    count = count + 1

    if count <= 3:
        if input_number.isdigit():
            input_number = int(input_number)

            if input_number == 0:
                print("you should enter a number more than 0")
                continue

            else:
                random_number = random.randrange(2, input_number)
                break

        else:
            print("You didnt input a number")
            continue

    else:
        player_want_to_play = False
        print("Probably you don't want to play")
        break


while player_want_to_play:
    random_input_number = input("guess a number: ")

    count = count + 1

    if count <= 3:
        if input_number = 

            input_number = int(input_number)

            if input_number == 0:
                print("you should enter a number more than 0")
                continue

            else:
                random_number = random.randrange(2, input_number)
                break

    if random_input_number.isdigit():
        random_input_number = int(random_input_number)
        
        if random_number == random_input_number:
            print("You got it, yeahhh 🎆🎉🎉")
            break

        elif random_input_number > random_number:
            print("Your guess is bigger than the actural number, try again 😀")
            continue

        else:
            print("Your guess is smaller than the actural number, try again 😀")
            continue

    else:
        print("You didnt input a number")
        continue