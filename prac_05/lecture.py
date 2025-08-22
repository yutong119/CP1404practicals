#1. Dictionaries
"""
Boolean: Ture = 1  False = 0

Ture + 3 = 4
False + 3 = 3

isinstance("string", str)
True

isinstance("string", int)
False

isinstance(False, int).  -------- also check parent classes
True

is_adult = True
isinstance(is_adult, int)
True
isinstance(is_adult, bool)
True
isinstance(3, bool)
False
"""
from mimetypes import guess_all_extensions


#2. Do this now
# names = open("names.txt", 'w')  #file——object操作文件的接口，而非直接存储文件内容的列表
# ages = open("ages.txt", 'w')
# names.write("Linda\nSindy\nAsh\nSin\n")
# ages.write("21\n23\n7\n10\n")
# names_lines = names.readlines()
# ages_lines = ages.readlines()
# names.close()
# ages.close()

# def find_oldest(names, ages):
#     # max(ages) 56
#     # ages.index(max(ages)) 2
#     return names(ages.index(max(ages)))

def find_oldest(names, ages):
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages):  # i是索引， age是元素值 生成一个包含索引（位置编号）和对应元素值的元组
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
    return names[oldest_index]

def run_tests():
    i = 0
    names = ["Bill", "Jane", "Sven"]
    ages = [21, 34, 56]
    print(find_oldest(names, ages))

run_tests()



#1. how to combine ages and names?  并行列表
names_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}
#2. Add and remove dictionary elements
"""To Add a new key_value pair:"""
    dictionary[key] = value
#if key exists in the dictionary, the value associated with it will be changed
"""To Delete a kry_value pair:"""
    del dictionary[key]
# if key is not in the dictionary, KeyError exception is raised
#3.
""" 
name_to_age["Bill"] #22
name_to_age["Bill"] += 1
name_to_age["Bill"] #23
"""
#4. Dictionary content methods
dictionary.keys() #all the keys
dictionary.values() #all. the values
dictionary.items() #all the key/value pairs as tuples