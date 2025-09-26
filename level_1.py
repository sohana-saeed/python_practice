# # Q1 – Ek Student class banao jisme attributes name, roll_number, aur marks hon. 
# # Phir ek method likho display_info() jo student ki information print kare.

# # Q2 – Ek Car class banao jisme attributes brand aur model hon. 
# # Ek method likho start() jo print kare Car started. Ek object banao aur method call karo.

# # Answer 01

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def display_info(self):
#         print(f"The name of student is {self.name}")
#         print(f"The roll number of {self.name} is {self.roll_number}") 
#         print(f"The maks of {self.name} is {self.marks}")

# s1 = Student("sohana", 426832, 490)
# s1.display_info()


# # Answer 02

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("The car started...")

car = Car("farari", "anything")
car.start()
