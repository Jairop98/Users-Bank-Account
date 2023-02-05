class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else: 
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
    
checkings = BankAccount(.04, 500)
savings = BankAccount(.1, 1000)

checkings.deposit(100).deposit(300).deposit(400).withdraw(500).yield_interest().display_account_info()
savings.deposit(200).deposit(900).withdraw(300).withdraw(200).withdraw(100).withdraw(200).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self
    
    def yield_interest(self):
        self.account.yield_interest()
        return self
    
Jairo = User("Jairo", "Jairop98")
David = User("David", "Davidb67")
Sarah = User("Sarah", "SarahP92")

Jairo.make_deposit(100).display_user_balance().make_withdrawal(500).display_user_balance().yield_interest().display_user_balance()
David.make_deposit(200).display_user_balance().make_withdrawal(300).display_user_balance().yield_interest().display_user_balance()
Sarah.make_deposit(900).display_user_balance().make_withdrawal(300).display_user_balance().yield_interest().display_user_balance()