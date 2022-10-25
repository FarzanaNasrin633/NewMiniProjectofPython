from curses import is_term_resized
from curses.ascii import isdigit
import random
from xml.dom import WRONG_DOCUMENT_ERR, WrongDocumentErr
 
input_number = input("Type a number: ")

guess_number = False

 while guess_number:
    print("Guess number is not correct")
    input_number = input("Do you want to try this again? ")
    guess_number = input_number == "yes"
    continue


if input_number.isdigit():
    input_number = int(input_number)

    if input_number == 0:
        print("you should enter a number more than 0")
        quit()


    random_number = random.randrange(2, input_number)

else:
    print("You didnt input a number")
    quit()


while True:
    random_input_number = input("guess a number: ")

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