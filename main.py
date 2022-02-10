# Nickname Generate by ____
import random

def main():
    # Program Variables
    nicknames = []
    firstName, lastName = setName()

    selection = 0
    while selection != "6":
        selection = getMenuSelection(firstName, lastName)

        if selection == "1":
            firstName, lastName = setName()
        elif selection == "2":
            randomNickname(firstName, nicknames, lastName)

    print("Goodbye")


# Declare Name
def setName():
    firstName = input("Print your firstname please: ")
    lastName = input("Print your lastname please: ")
    return firstName, lastName


def getMenuSelection(firstName, lastName):
    # Create Main Menu
    print(f'''
    Main Menu ({firstName} {lastName})
        1. Change Name
        2. Display a Random Nickname
        3. Display All Nicknames
        4. Add a Nickname
        5. Remove a Nickname
        6. Exit''')
    return input("Type a number corresponding with it's option please: ")


def randomNickname(firstName, nicknames, lastName):
    nick = random.choice(nicknames)
    print(f'{firstName} "{nick}" {lastName}')


# Call main to begin program
main()