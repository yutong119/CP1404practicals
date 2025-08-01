"""1. overwriting: child overwrite parents class
如果想call parent class, need add super.  like: staff_1.super.__init__"""

"""2"""
# #父类
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name} 发出声音")
#
#
# # 子类（继承自 Animal）
# class Dog(Animal):
#     def speak(self):  # 重写父类方法
#         print(f"{self.name} 汪汪叫")
#
#
# # 子类（继承自 Animal）
# class Cat(Animal):
#     def speak(self):  # 重写父类方法
#         print(f"{self.name} 喵喵叫")
#
#
# # 使用继承
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
#
# dog.speak()  # 输出: Buddy 汪汪叫
# cat.speak()  # 输出: Whiskers 喵喵叫

"""3"""
#str convert object to string

"""4"""
"""
from datatime import datetime
from jcu_number import JcuMember

class Staff(JcuMember):
    def __init__(self, 1, 2, **kwargs):
        super().__init__(**kwargs)
        剩下的照常写self.1 = 1
        self.2 = 2
        
            #如果这个函数全部传入父类的object呢，就全部写kwargs就行了
            def display_friuts(**kwargs):
                print(kwargs, type(kwaegs))
                
    def __str__(self):
        return f"{super().__str__()} Staff ID: .........}"
        
    def calculate)annual_salary(self):
        return f"{self.salary *12:.2f}"
        
      
   对于子类用于测试创建的物品，要包含所有的包含父类元素， 父类的话只写自己有的就行     
"""

"""5 注意⚠️create another py file to text, assignment2 里面要注意"""

"""6 在编写测试的py file时，不需要再次插入父母类，因为子类已经插入过了， 要插入父母类也只是只用父母类的物品"""

"""7 
Aggregation（聚合）
核心特点：
弱拥有关系：整体与部分的生命周期相对独立，部分可以属于多个整体。
部分可以在整体之外存在：整体被销毁时，部分不会被强制销毁。
示例：图书馆（整体）与书籍（部分），书籍可以在图书馆之外存在。
"has a"  "contain a"

class Book: (必须先存在）
    def __init__(self, title， author):
        self.title = title
        self.author = author
        
class library:
    def __init__(self, name):
        self.name = name
        self.book = []
        
    def add_book(self, book):
        self.books.append(book) 
        
# class Library:
#     def __init__(self, books=None):
#         # 图书馆通过参数接收书籍列表，不控制书籍的生命周期
#         self.books = books or []  # 聚合关系：Library 包含 Book
# 
#     def add_book(self, book):
#         self.books.append(book)

# # 使用示例
# book1 = Book("Python Crash Course")
# book2 = Book("Clean Code")
# 
# library = Library([book1, book2])  # 书籍可以独立存在
# library.add_book(book1) 
# library.add_book(book2)

一个文件里不能有两个类，写作业和考试时注意
"""

"""8
Composition（组合）
核心特点：
强拥有关系：整体与部分的生命周期紧密绑定，部分不能独立于整体存在。
部分的创建和销毁由整体控制：整体被销毁时，部分也会被销毁。
示例：汽车（整体）与发动机（部分），发动机不能独立于汽车存在。
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

class Car:
    def __init__(self):
        # 汽车直接创建发动机实例，控制其生命周期
        self.engine = Engine("gasoline")  # 组合关系：Car 拥有 Engine

# 使用示例
car = Car()
# 当 car 被销毁时，其 engine 也会被销毁  
"""

"""9 IndexError 要熟悉使用expect"""

"""10 circle and rectangle is same level"""

"""11 math model import pi"""

"""12 bound and unbound method"""
#call the class, call the method, pass  object? into the method

# name = "Sam"
# name.upper() bound
# string.upper(name) unbound

"""13"""
"""做这个绑定和不绑定的题
1. Car.drive(my_car, 30)
may_car = Car()
my_car.drive(30)

object.method(p)

2. str.upper(name)
name = str()
name.upper()

3. Fish.swim(namo)

4. my_car.add_fule(60)"""

"""14
Arbitrary(object) 记住Arbitrary是父母类， 不是object"""

"""15 
class SubClass(SuperClass):
    def __init__(self, **kwargs)
        super().__init__(**kwargs)
"""

"""16
vars function will return dictory"""