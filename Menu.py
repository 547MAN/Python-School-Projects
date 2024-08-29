class Menu():
    def __init__(self):
        #The "Menu" class should only have one property which is a list of options.
        #------------
        #A list object:
        self.menu=[]
    def add_option(self):
        #And all the options should be added to that list using the add_option() method after you create a menu object.
        #------------
        #I understood this one as following : "User has to write in the options which will be added to the self.menu list"
        # That seems to tedious, so I got with the gut feeling of that I understood that wrong and added the options myself.
        
        #------------
        #Append the list the menu list with corresponding keys/values.
        self.menu.extend([
            "1 Open a new account",
            "2 Deposit money into your account",
            "3 Withdraw money from your account",
            "4 Add interests to your account",
            "5 Get the current balance of your account",
            "6 Quit"]
        )
        self.userOptionInput = None
        print("--------------------------------------------------------")
        print("\nWelcome to High Top Bank")
        print("Please select the option you would like to work with")
        print("--------------------------------------------------------")
        print("\nP.S: Press the correspending number on your keyboard\n")
        print("--------------------------------------------------------\n")
        
    def get_input(self):
        #Also, the get_input() method should display all the options in the menu and ask the user to enter his/her option.
        
        #------------
        #I take the items from the list
        for option in self.menu:
            print(option)
        print("--------------------------------------------------------")
        self.userOptionInput = input("Enter your option: ")
        print("--------------------------------------------------------")




