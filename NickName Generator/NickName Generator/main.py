# Nickname Generator by Omar Elshimi
import random

#Main Array
nicknames = ["Tyrannosaurus", "Stegosaurus", "Triceratops", "Velociraptor",
    "Spinosaurus", "Allosaurus", "Archaeopteryx", "Dilophosaurus", "Brachiosaurus"]

#Main Function
def main():
    # Program Variables
   
    firstName, lastName = setName()

    selection = 0
    while selection != "6":
        selection = getMenuSelection(firstName, lastName)

        if selection == "1":
            firstName, lastName = setName()
        elif selection == "2":
            randomNickname(firstName, nicknames, lastName)
        elif selection == "3":
            allNickname()
        elif selection == "4":
            addNickname()
        elif selection == "5":
            removeNickname()
        elif selection == "6":
            print("Program Closed")

# Declare Name
def setName():
    firstName = input("Print your firstname please: ")
    lastName = input("Print your lastname please: ")
    return firstName, lastName

#Menu Function
def getMenuSelection(firstName, lastName):
    # Create Main Menu
    print(f'''
    Main Menu ({firstName} {lastName})
        1. Change Name
        2. Display a Random Nickname
        3. Display All Nicknames
        4. Add a Nickname
        5. Remove a Nickname
        6. Exit
        ''')
    return input("Type a number corresponding with it's option please: ")

#Random Nickname Function
def randomNickname(firstName, nicknames, lastName):
    nick = random.choice(nicknames)
    print(f'{firstName} "{nick}" {lastName}')

#Display All Nicknames
def allNickname():
    for x in nicknames:
        print(x)

#Add Nickname Function
def addNickname():
    nick = input("Print the nickname you would like to add: ")
    nicknames.append(nick)
    print(nick + " added")

def removeNickname():
    allNickname()
    nick = input("Print the nickname you would like to remove: ")
    if nick in nicknames:
        nicknames.remove(nick)
        print(nick + "removed ")
    else: 
        print("Nickname not found")
    
# Call main to begin program
main()

