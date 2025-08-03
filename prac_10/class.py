"""1. infinite loop: while loop   (1 mark)"""
# name = input("Enter name: ")
# while name == "":
#     print("Invalid Input")

#--------------------------------------------------------------------------------------
"""2. list  (1 mark)"""
# x = [10, 12, 14, 16, 18]  #list
# y = x  #assign into y, y also list
# print(x)
# print(y)
# z = x[:]  # copy x paste into z (create a copy of list x assigned to z)
# print(z)  #‼️same argument doesn't mean same object
# # a = [10, 12, 14, 16, 18]
# print(z == x)
# print(x == y)
# print(x is y)
# print(x is z)  #‼️same argument doesn't mean same object  #output is False

#--------------------------------------------------------------------------------------
"""3. for loop """
# z = 4
# for x in range(1, 5):
#     print("*" * z)
#     if x < z:
#         z = z- 1
#output:
# ****
# ***
# **
# **

#--------------------------------------------------------------------------------------
"""4. Understand ::, pop, remove"""
# numbers = list(range(6))   #start 0, end with 6.
# print(numbers)             #[0, 1, 2, 3, 4, 5]
# print(numbers[::])         #它的完整格式是 [start:stop:step]
# print(numbers[:4:])
# print(numbers[1::])
# print(numbers[-2::-2])
# print(numbers[5])
# print(numbers[len(numbers)])
# print(numbers.pop()) # last element to be deleted when did not indicate the index
# print(numbers.pop(2))
# print(numbers)
# numbers[2] = numbers.pop()
# print(numbers)
# numbers.remove()

#--------------------------------------------------------------------------------------
"""5.例子 Write a function to print the below output
        Call: print(test(4, "xyz"))
        Output: xyzxyzxyzxyz
"""
# def test(times, string):
#     return times * string

#--------------------------------------------------------------------------------------
"""6. """
# def get_number(x=2, y=10):
#     return x * 4 - y
# print(get_number())            #-2 (if no parameter, will print the dfault value)
# print(get_number(3, 1))  #11
# print(get_number(get_number(3,1)))
# print(get_number(11))          #只有一个值的话，传入这个值，另一个值用默认值

#--------------------------------------------------------------------------------------
"""7. All the Error"""
# #IndexError
# # print(numbers[len(numbers)])
#
# #ValueError
# a = "e"
# print(2 * int(a))
#
# a = "1.1"
# print(int(a))
#
# #NameError
# x = "apple"
# print(g)
#
# #ZeroDivisionError
# number = 0
# print(10/number)
#
# #⚠️例子：注意读题目，有时候让说print什么，不是说什么Error
# try:
#     number = int(input("Enter number: "))
#     print(10 / number)
#     剩下的在手机上

#--------------------------------------------------------------------------------------
"""8. dictionary, unmutiable?????????不可换顺序？？？"""

#key不可以是一样的， value可以是一样的
#
# dictionary_pairs = {"sam": 23456, "lukas": 34567, "Lea":3489}
#
# dictionary_pairs["dior"] = 34567
# print(dictionary_pairs)
# dictionary_pairs["dior"] = 99999
# print(dictionary_pairs)
# print(dictionary_pairs.keys())
# print(dictionary_pairs.values())
# print(dictionary_pairs.items())
# for name, number in dictionary_pairs.items():
#     print(f"{name:<8} number is {number:>8}") # ------ Assignment1 这些<, > 符号的使用，找到keys和values各自的最大长度

#--------------------------------------------------------------------------------------
"""9. Inheration"""
# class Arbitrary(object):
#     def __init__(selfself, data=0):
#         self.number = data
#
#     def
#     剩下的在手机上
#

#--------------------------------------------------------------------------------------
"""10. assert在手机上"""

#--------------------------------------------------------------------------------------
"""11. check how many Uppercase you have, use for loop , is_uppercase? """



