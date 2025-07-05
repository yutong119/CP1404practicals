from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

#create a new list that contains these three existing ProgrammingLanguage objects
collections = [python, ruby, visual_basic]
#Loop through and print the names of all the languages with dynamic typing
print("The dynamically typed languages are:")
for i in collections:
    if i.is_dynamic():
        print(i.name)

