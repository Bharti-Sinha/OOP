# create a class to model bank account

class Account:
    # what would differentiate one account from another
    accID = None
    name = None
    balance = 0

    # what are the operations in a bank account
    def deposit(self, amount):
        # Formal parameters are used for passing arguments. They come into existence only when method is invoked.
        # amount is a formal parameter
        self.balance += amount
        return

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return True # helps with debugging
        else:
            print("The balance is low")
            return None

    def show_balance(self):
        return self.balance

    def transfer(self, account, amount):
        if self.balance >= amount:
            self.balance -= amount
            account.deposit(amount)
            # account.balance += amount # this is bad practice, always make changes to attributes using methods
            # the deposit method may have other criticial methods before any change is made to balance attribute , e.g, authentication.
            return True
        else:
            return None


# Assign values to both accounts
mum = Account()  
dad = Account()

print(mum)
print(dad)
print(Account)

# Not a typical OOP approach
mum.accID, mum.name, mum.balance = "s123", "Mercy Brown", 1000
dad.accID, dad.name, dad.balance = "g234", "David Brown", 5000

print("The amount in mum's balance before deposit: ", mum.balance)
mum.deposit(1000)
print("The amount in mum's balance after deposit: ", mum.balance)

print("The amount in dad's balance before withdrawal: ", dad.balance)
dad.withdraw(100)
print("The amount in dad's balance after withdrawal ", dad.balance)

print("The amount in dad's balance before transfer: ", dad.balance)
dad.transfer(mum, 900)
print("The amount in dad's balance after transfer ", dad.balance)
print("The amount in mum's balance after transfer ", mum.balance)

print("Mom's balance is $ ", mum.show_balance())
print("Dad's balance is $ ", dad.show_balance())

# # One of the ways to assign variables
# mum = Account("s123", "Mercy Brown", 1000)
# dad = Account("g234", "David Brown", 5000)
