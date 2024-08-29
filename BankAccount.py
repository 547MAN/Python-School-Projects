from Menu import Menu

class BankAccount(Menu):
    
    def __init__(self):
        super().__init__()
        self.add_option()
        self.get_input()
        
    
    
    def newUser(self):
        print("--------------------------------------------------------")
        print("New account logged in and accesed!\n")
    
        self.menu.pop(0)
        self.get_input()
        #Recalls the method to select menu options if user inputs 1
        self.userInputAction()
        
        
    def deposit(self):
        print("Depositing money")
    def withdraw(self):
        print("Withdrawing money")
    def add_interest(self):
        print("Adding interest rate")
    def get_balance(self):
        print("Showing balance")

    def quitMenu(self):
        print("Quitting the program")
        
    def userInputAction(self):
        if self.userOptionInput=="1":
            self.newUser()
        elif self.userOptionInput=="2":
            self.deposit()
        elif self.userOptionInput=="3":
            self.withdraw()
        elif self.userOptionInput=="4":
            self.add_interest()
        elif self.userOptionInput=="5":
            self.get_balance()
        elif self.userOptionInput=="6":
            self.quitMenu()

bank = BankAccount()
bank.userInputAction()