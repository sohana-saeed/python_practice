# # Q3 – Ek Book class banao jisme constructor ho aur attributes title, author, aur price ho. 
# # Ek method show_details() banao. Phir do objects banao aur details show karo.

# # Q4 – Ek BankAccount class banao jisme account_number, holder_name, aur balance ho. 
# # Methods deposit() aur withdraw() banao jo balance update karein.

# # Answer 03

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def show_details(self):
#         print(f"The title of book is '{self.title}'")
#         print(f"The author of book is '{self.author}'")
#         print(f"The price of book is {self.price} Rs")

# b1 = Book("The Art of thinking", "sohana saeed", 1000 )
# b2 = Book("The real beauty", "sohaa sona", 1500 )

# b1.show_details()
# b2.show_details()

# # Answer 04

class BankAccount():
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        return f"The amount {amount} has been deposited \nThe total balance is {self.balance + amount}"
    
    def withdraw(self, amount):
        return f"The amount {amount} has been withdraw \nThe total balance is {self.balance - amount}"

acc1 = BankAccount(1914, "sohana saeed", 1000)

print("The total balance is", acc1.balance)
print(acc1.deposit(500))
print(acc1.withdraw(400))
