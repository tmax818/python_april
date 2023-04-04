class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance 
        pass  #(remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    
    def deposit(self, amount):
        self.balance =+ amount
    
    def withdraw(self, amount):
        pass
    
    def display_account_info(self):
        print(f"You have a balance of: ${self.balance}")
        print(f"Your current interest rate is: {self.int_rate * 100}%")
    
    def yield_interest(self):
        pass
acct1 = BankAccount()
acct2 = BankAccount(.1, 1000000)
acct1.deposit(1000)
acct1.display_account_info()