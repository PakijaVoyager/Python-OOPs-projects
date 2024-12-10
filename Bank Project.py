import sys #This module provides many functions to manipulate different python run time environment
class BankAtm: #Initializing class name
    def __init__(self): #Initializing constructor
        self.balance = 0
        self.pin = 0
        print(type(self.pin))
        self.menu() #Calling menu method in the constructor to call it automatically when the object is created
        
    def menu(self): #This method calls different methods according to user requirement
        usr = int(input('''
        Hi! There how can I help you.
        a. Press 1 to create pin.
        b. Press 2 to change pin.
        c. Press 3 to add balance.
        d. Press 4 to withdraw balance.
        e. Press 5 to see the remaining balance.
        g. Press 6 to exit.
         '''))
        if usr == 1:
            self.CreatePin()
        elif usr == 2:
            self.ChangePin()
        elif usr == 3:
            self.AddBalance()
        elif usr == 4:
            self.WithdrawBalance()
        elif usr == 5:
            self.RemBalance()
        elif usr == 6:
            sys.exit()
        else:
            print("Not in the option")
            self.menu()
            
    def CreatePin(self):
        pin = int(input("Enter your new pin : "))
        print("Your pin created successfully")
        self.pin = pin
        self.menu()
    
    def ChangePin(self):
        pins = int(input("Enter your current pin : "))
        if pins == self.pin:
            new_pin = int(input("Enter your new pin : "))
            new_pin2 = int(input("Renter your pin : "))
            if new_pin == new_pin2:
                self.pin = new_pin2
            else:
                print("Pin does not match")
                self.ChangePin()
        else:
            print("Unmatched pin")
            self.ChangePin()
        self.menu()
            
    def AddBalance(self):
        pin = int(input("Enter your pin : "))
        if pin == self.pin:
            balance = int(input("Enter the amount : "))
            self.balance+=balance
            print("Balance added successfully")
        else:
            print("Pin does not match")
            self.AddBalance()
        self.menu()
    
    def WithdrawBalance(self):
        pin = int(input("Enter your pin : "))
        if pin == self.pin:
            balance = int(input("Enter the amount : "))
            if balance < self.balance:
                withdraw = self.balance - balance
                print(f"Rs. {withdraw} is withdrawed successfully")
                self.balance = withdraw
            else:
                print("You do not have sufficient balance to withdraw")
                self.WithdrawBalance()
        else:
            print("Pin does not match")
            self.WithdrawBalance()
        self.menu()
    
    def RemBalance(self):
        pin = int(input("Enter you pin : "))
        if pin == self.pin:
            print(f"Your remaining balance is Rs.{self.balance}")
        else:
            print("Unmatched pin")
            self.RemBalance()
        self.menu()
    
    
        
    
first = BankAtm()