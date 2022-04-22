# Creater: Jasmine Ross
# Completion date: 03/23/22
# Name: Adventure Game

# import modules and use functions from those modules
import time
import random

# UP
room = "You run to your room, lock the door and call 911.\n " +\
       "You live to see another day!"
kidnap = "You run to your room and come face to face with a burglar. " +\
         "Now you have to fight.\n You did't make it!"
cat = "Oh good it was just your cat."
# DOWN
back = "You run downstairs and back out the front door to call 911.\n" +\
       "You live to see another day!"
kitchen = "You run downstairs to the kitchen to see a " +\
          "kidnapper and get kidnapped.\n" +\
          "You did't make it!"
dog = "Oh good it was just the dog. "


def print_pause(message):
    print(message)
    time.sleep(2)


# code inclues  at least four functions
def intro():
    print_pause("You just got off work and it has been one long day.")
    print_pause("You walk in the front door and head upstairs to your room.")
    print_pause("Halfway up the stairs you hear a noise.")
    print_pause('You stop and you whispa "what was that?"')


def option_up():
    choice1 = random.choice([room, kidnap, cat])
    print("")
    print_pause(choice1)
    print("")


def option_down():
    choice2 = random.choice([back, kitchen, dog])
    print("")
    print_pause(choice2)
    print("")


def validate(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def make_choice():
    choice = validate("Are you going to run up or down the stairs?\n"
                      "Type down or up. ", ['down', 'up'])
    if 'down' in choice:
        option_down()
    elif 'up' in choice:
        option_up()


def play_again():
    accept = input("would you like to play again?\nType yes or no: ").lower()
    while True:
        if accept in ["y", "yes"]:
            print_pause("")
            print_pause("Awesome! Lets play again.")
            print_pause("")
            return True
        elif accept in ["n", "no"]:
            print_pause("")
            print_pause("Thanks for playing!")

            return False
        accept = input("Not a valid entry.\n"
                       "Please choose yes or no: ").lower()


while True:
    intro()
    print_pause("")
    make_choice()
    print_pause("")
    if not play_again():
        break
