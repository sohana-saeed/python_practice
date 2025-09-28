# Q9 – Upar wale Animal example me polymorphism use karo: 
# ek loop likho jo Dog aur Cat objects pe sound() call kare.

# Q10 – Ek Shape class banao jisme ek method area() ho.
#  Phir Circle aur Square classes banao jo Shape se inherit karein aur apna apna area() calculate karein.


# Answer 09

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

animals = [dog, cat]
for animal in animals:
    animal.sound()


# Answer 10
# Ek Shape class banao jisme ek method area() ho.
#  Phir Circle aur Square classes banao jo Shape se inherit karein aur apna apna area() calculate karein.

class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def area(self, radius):
        print("The area of circle is", 3.14*(radius**2))
class Square(Shape):
    def area(self,length):
        print("The area of square is", length*length)

circle = Circle()
circle.area(2)
square = Square()
square.area(2)

