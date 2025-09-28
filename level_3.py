# # Q5 – Ek Employee class banao jisme private attribute _salary ho. 
# # Ek getter aur setter banao get_salary() aur set_salary() taake salary ko read aur update kiya ja sake.

# # Q6 – Ek Rectangle class banao jisme length aur width private ho aur methods area() aur perimeter() ho.

# # Answer 05

# class Employee:
#     def set_salary(self, __salary):
#         self.__salary = __salary

#     def get_salary(self):
#         return f"The salary is {self.__salary}"
    
# E1 = Employee()
# E1.set_salary(500000)
# print(E1.get_salary())

# # Answer 06

class Rectangle:
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def area(self):
        return f"The Area of rectangle is {(self.__length) * (self.__width)}"

    def perimeter(self):
        return f"The perimeter of rectangle is {(self.__length + self.__width) * 2}"
    
    def get_values(self):
        print(self.area())
        print(self.perimeter())

a = Rectangle(2,5)
a.get_values() 

