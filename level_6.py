# Q11 – Ek Author class banao aur ek Book class banao jisme Author ka object as an attribute ho (Composition).
# Book ka show_details() author ka name bhi print kare.

# Q12 – Ek Vector class banao 
# jisme dunder method __add__ implement karo taake v1 + v2 likhne se vectors add ho jayein.

# Answer 11

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author

    def show_details(self):
        print("The book title is:", self.title)
        print("The book author is:", self.author.name)

author1 = Author("Sohana")
book1 = Book("The art", author1)

book1.show_details()


# Answer 12

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        return f"{self.i + other.i}i, {self.j + other.j}j, {self.k + other.k}k"
    
v1 = Vector(1,2,3)
v2 = Vector(1,2,3)
vector = v1 + v2
print(f"The vector is ({vector})")