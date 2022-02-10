
#Declare Name
def setName():
    firstName = input("Print your firstname please: ") 
    lastName = input("Print your lastname please: ")
setName()

selection = 0

def main():
    while selection != 6:
        #Create Main Menu
        print('''
        Main Menu
            1. Change Name
            2. Display a Random Nickname
            3. Display All Nicknames
            4. Add a Nickname
            5. Remove a Nickname
            6. Exit''')
        selection = input("Type a number corresponding with it's option please: ")
        if selection == 1:
            setName() 
main()
