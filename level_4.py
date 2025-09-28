# # Q7 – Ek parent class Person banao jisme name aur age ho aur ek method show_info().
# #  Phir ek child class Teacher banao jo Person se inherit kare aur extra attribute subject ho.

# # Q8 – Ek parent class Animal banao aur ek method sound(). 
# # Phir child classes Dog aur Cat banao jo apna apna sound print karein.

# # Answer 07

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def show_info(self):
#         print(f"The name is {self.name}")
#         print(f"The age is {self.age}")
#         print(f"The subject is {self.subject}")

# sho = Teacher("sohana", 17, "maths")
# sho.show_info()




# Answer 08

class Animal:
    def sound(self):
        print("Animal makes sound!")
class Dog(Animal):
    def sound(self):
        print("Dog say:","Bow Bow!")
class Cat(Animal):
    def sound(self):
        print("Cat say:","Meow Meow!")

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()