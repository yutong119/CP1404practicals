"""1. Write code that asks the user for their name, then opens a file called name.txt
and writes that name to it. Use open and close for this question."""
user_name = input("Enter your user name: ")
out_file = open("name.txt", 'w')
print(f"{user_name}", file=out_file)
out_file.close()

"""2. In the same file, but as if it were a separate program, write code that opens "name.txt" 
and reads the name (as above) then prints (note the exact output),"""
in_file = open("name.txt", 'r')
name = in_file.read()
print(f"Hi {name.strip()}!")
in_file.close()

"""3.Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints 
the result, which should be... 59. Use with instead of open and close for this question."""
with open("numbers.txt", 'w') as out_file:
    out_file.write("17\n42\n400")

with open("numbers.txt", 'r') as out_file:
    lines = out_file.readlines()
    number1 = int(lines[0].strip())
    number2 = int(lines[1].strip())
    print(number1+number2)


"""4. Now write a fourth block of code that prints the total for all lines in numbers.txt. 
This should work for a file with any number of numbers. Use with instead of open and close for this question."""
with open("numbers.txt", 'r') as out_file:
    total = 0
    for line in out_file:
        total += int(line.strip())
    print(total)