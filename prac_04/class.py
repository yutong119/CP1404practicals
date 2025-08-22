"""
1. 列表你要知道，，，
element
index
from 0 to
can be any type

2.
列表也有构造函数，可以把 转化成列表
letters = list("Things")

or 使用[]也可以

3.
lists, tuples, and string 都是有序序列
lists是可更改的
tuples， 和strings 是不可更改的，想要更改就要重新创建
A set是无序集合

4. for singular in plural
注意命名

5.
sum()
"""

# #6. do this now
# names = ["Linda", "Bob", "Sindy", "candy"]
# number = int(input(f"Enter number, up to {len(names)}: "))
# try:
#     print(names[number - 1])
# except IndexError:
#     print("Invalid number")


"""
1. len min max sum
average == sum()/len()

2. 从list移走一个元素
del scores[1]  ------ 根据index移走
scores.remove(1) ------ 根据数值移走

3. append(item)
    sort()  将列表中的元素按升序排列 - return the results as a list
    reverse() 反转列表中元素的顺序
    count(1) 数这个数值的个数
    
    letters = sorted('hi mum')
    Gives [' ','h','i','m','m','u']
    
    list(reversed(things))
    
    things = [10, 4.5, 1, 1, 1, 1]
    things.remove(1) 只会移走第一个1

4. 
if ,,,, in,,,,,,
if,,,,, not in ......  

5. 
subjects = ["CP1401", "CP1404"]
for subject in subjects:
    print(subject)

6. list是可变的，所以关于list的更改，应该在专门的函数里进行，而不应该放在主函数里
like：
def main():
    numbers = [1, 2, 3]
    add_offset(numbers, 2)
    print(numbers) #print [3, 4, 5]
    
def add_offset(elements, offset):
    for i in range(len(elements)):
        elements[i] += offset
        
7. Nested Lists
data = [['Derek', 7], ['Carrie', 8], ['Bob',6], ['Aaron',9]]

8. How to index lists of lists
things = ['a', [1,2,3], 'z']
things[1][0]
things[1]
[1,2,3][0]
"""




"""CLASS EXAMPLE"""
"""1. 删除 name from names, until the list is empty """

# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# name_to_remove = input("Who do you want to remove?")
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print("Must enter the valid name")
#     print(names)
#     name_to_remove = input("Who do you want to remove?")
# print(names)


"""2. EXAM: Whether or not a person is a mutant"""

'''3. 看看哪里有错'''
# with open("numbers.txt", "r") as input_file:  #why need to create file_object: is to access file
#     numbers = input_file.readlines()          #read data to a list， turn into a list
#
#     """以上是read data, 以下是process data"""
#
# sum_of_numbers = 0
# for number in numbers:
#     sum_of_numbers += float(number)
# print(f"Total sum of numbers is {sum_of_numbers}")

"""4. 为什么add_offset不用return数值，因为它自己在函数里面把预案来的函数值更改了"""
# def main():
#     numbers = [1, 2, 3]
#     add_offset(numbers, 2)
#     print(numbers)  # print [3, 4, 5]
#
#
# def add_offset(elements, offset):
#     for i in range(len(elements)):
#         elements[i] += offset

"""5. Index error"""

# """6. 一些函数 reverse, max, sort, len. """
# from operator import itemgetter  # 导入 itemgetter
#
# # 定义嵌套列表数据，模拟人员姓名和年龄
# data = [["Eileen", 25], ["Kelly", 29], ["Edward", 18]]
#
# # 打印第一个子列表（完整人员信息）
# print(data[0])
# # 打印第一个子列表的第二个元素（年龄）
# print(data[0][1])
#
# # 按子列表第一个元素（姓名）默认升序排序（原地修改 data）
# data.sort()
# # 打印按姓名排序后的结果
# print(data)
#
# # 按子列表第二个元素（年龄）倒序排序，需用 itemgetter 指定索引
# # sorted 会返回新列表，重新赋值给 data
# data = sorted(data, key=itemgetter(1), reverse=True)
# # 打印按年龄倒序排序后的结果
# print(data)
#
# """7. Tuples"""
# # age = (12, 13, 14, 56, 99)
#
# """8. EXAM"""
# words = "This is Python"
# print(words)
# words = words.split()
# print(words)
#
# for word in words:
#     print(word, )
#
#
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(numbers)
# print([number * 2 for number in numbers])
# =
# list_numbers=[]
# for number in numbers:
#     new_number =number * 2
#     list_numbers.append(new_number)
# print(list_numbers)
# print([number for number in numbers if number > 50])
# print([number *2 for number in numbers if number > 50])
# print(number for number in numbers if number < 20)
# print([number/2 for number in numbers if number > 20])
#
# words =
#
# chars = "Hi THERE Mum"
#
# cars =[["Audi", 2006], ["Jaguar", 2022], ["BMW", 2019], ["Aston MArtin", 2018]]
# print([car for car in cars])
# print([tuple(car) for car in cars])
# print(f"{car[0]}" for car in cars)
# print([car[0] for car in cars if car[1] > 2017])
#
# """9. """
# s = "Hello world   Python"
# result = s.split()
# print(result)
# #['Hello', 'world', 'Python']

"""10, """
# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
# def get_numbers():
#     number = int(input("Please enter number:"))
#     numbers = number.split(',')
#     numbers.append(number)
#     return numbers
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i]**2
#
# def display_numbers(numbers):
#     # print(sorted(numbers))
#     print("..".join([str(number) for number in sorted(numbers)]))
#
# main()

"""11.考试一定会考"""
numbers = [12, 15, 30]
new_numbers = numbers #把numbers的值重新储存在new_numbers
price_numbers = [12, 15, 30]
print(numbers)
print(new_numbers) #print一样的
print(numbers is new_numbers)
print(numbers is price_numbers)

numbers.append(50)
print(numbers)
print(new_numbers)
print(price_numbers)

things = []
for x in range(1, 4):
    for y in range(1, 4):
        print(f"{x} + {y} = {x + y}")
        things.append(x+y)
print(things)
print([x + y for x in range(1, 4) for y in range(1, 4)])

s = "hello WORLD"
print(s.capitalize())  # 输出: "Hello world"

"""12, 这个考试也会考"""
datas = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# for name, score in datas:
#     print(f"{name:<10}= {score}")
#     #将name左对齐并且占用10个字符的宽度
#     # print([max(datas[1]) for datas[1] in datas if max(datas[1]) ])
name_width = max()

isinstance(1, int) #这个是检查t是不是int的 True  isinstance() isinstance() isinstance()
Boolean 里面的True and False 可以被认为1 和 0













