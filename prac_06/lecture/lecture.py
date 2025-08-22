"""1"""
# products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
#
# on_sale_products = [product for product in products if product[2]]
# print(on_sale_products)
# #["PC", 1420.95, True], ["Plant", 24.5, True]
# for thing in products[0]:
#     print(thing)
#     #Phone
#     #340
#     #False

"""2"""
class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale
        # self._is_stolen = False

    def __str__(self):
        if self.is_on_sale:
            on_sale_string = "(on sale)"
        else:
            on_sale_string = ""
        return f"{self.name}, ${self.price:.2f} {on_sale_string}"

    def __repr__(self):
        return str(self)

    def put_on_sale(self, discount_percentage):
        """Put Product on sale by discount_percentage as decimal (e.g.,)"""
        self.price * (1 - discount_percentage)
        self.is_on_sale = True

p = Product("Phone", 340, False)
print(p.name, "...")
print(p)
p.put_on_sale(0.1)
print(p)
# p._is_stolen = True

products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]

on_sale_products = [product for product in products if product.is_on_sale]
print(on_sale_products)

"""3"""
class Student: #calss header
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"

#Simple example class usage (client code)
first_name = input("First name: ")
last_name = input("Last name: ")
student_id = int(input("ID: "))
s1 = Student(first_name, last_name, student_id)
print(s1.first_name, "has ID", s1.id)

"""4
class name should use the CapWords convention: StudentRecord
Method names should follow the same convention as function name : set_value"""

"""5 EXAM: identify the class name 骆驼写法 Coffee. shop.py 文件名字"""

"""6"""
class Monitor:
    """A class to represent a monitor with specified model, width, height"""

    def __init__(self, model: str, width: int, height: int):
        """Initialize a new instance of Monitor class"""
        self.model = model #local variable  #self.model = instance variable
        self.width = width
        self.height = height  #instance variable id belongs ro class

    def get_resolution(self) -> tuple:
        """Return the tuple of width and height"""
        return self.width, self.height

    def get_total_pixels(self) -> int:
        """Calculate and return the number of pixels"""
        return self.width * self.height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


#test
from 文件名 import class名字
monitor1 = Monitor("MAX", 20, 90)         #model is object
monitor2 = Monitor("SANDY", 55, 66)

print(monitor1) #print function doesn't

print(monitor1.get_resolution())
print(monitor2.get_resolution())

print(monitor1.get_total_pixels())
print(monitor2.get_total_pixels())

print(monitor1 == monitor2)
assert monitor1 == monitor2 #do testing during development


"""7"""
numbers = [1, 2, 3, 4, 5]
print(dir(numbers))

myList = [1, 2, 3]
print(type(myList))

number = 10
print(type(number))

text = ""
print(type(text))


x = isinstance(5, int)
print(x)        #return Ture

x = isinstance("5", int)
print(x)     #return False


a = 4
b = 5
c = "hello"
d = "python"
e = (9, 7)
f = (9, 9)

print(a+b) #9
print(c+d) #hello python
print(b*c) #hellohellohellohellohello
print(a+c) #cannot
print([2, 3] * 3) #[2, 3, 2, 3, 2, 3]
print(e + f) #(9, 7, 9, 9)

"""8 magic method"""
class Point:
    """"""
    def __init__(self, x=0.0, y=0.0):
        """"""
        self.x = x #variable can store only one object
        self.y = y

    def __str__(self):    #convent object to the str format  __str__cannot store a list of object, but repr can
        # __str__ also can la, but need use for loop to store the list
        return f"{self.x} {self.y}"

    def __repr__(self):
        return f"{self.x} {self.y}" #x, y is list name

    def __add__(self, other):
        return Point(self.x + other.x, )

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __gt__(self, other):
        return

    def __ge__(self, other):
        return self.x >= other and other.y >= other

    def __mul__(self, other):
        """Multiply"""
        return Point(self.x * other.x, self.y * other.y)

    def __sub__(self, other):
        """Subtraction"""
        return Point(self.x - other.x, self.y - other.y)

here = Point(5,4)
there = Point(4, 4)
print(here < there)

"""9 example"""
class Word:
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __add__(self, others):
        return self.string + others.string

"""10 prac"""
class User:
    """"""
    def __init__(self, name=""):
        """In"""
        self.name = name
        self.tacos = 5
        self.score = 0

    def __str__(self):
        return f"{self.name}, {self.score} points, {self.tacos} tacos left"

    def give_tacos(self, others):
        if self.tacos > 0:
            self.tacos -= 1
            self.score += 1
        else:
            print("there is no tacos left to give!")











