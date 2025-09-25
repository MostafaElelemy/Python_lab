import math
# - write a program that prints hello world
print("hello world")
# 	- application to take a number in binary form from the user, and print it as a decimal
bi_num =input("Enter a binary number: ")
f=0
for i in bi_num:
    if i != '1' and i != '0':
        f=1
        break
if f==1:
    print("plz enter 0 or 1")
else:
    print(int(bi_num,2))

# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"
def div(number): 
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return " enter a another number"
number = input("Enter a number: ")
if number.isnumeric():
    print(div(int(number)))
else:
    print("enter a valid number ")
# 	- Ask the user to enter the radius of a circle print its calculated area and circumference
try:
    radius = float(input("Enter the radius:"))
    if radius > 0:
        area = math.pi * radius ** 2
        circum = 2 * math.pi * radius
        print("area :", area)
        print("circumference :", circum)
    else:
        print("Radius must be positive")
except ValueError:
    print("Invalid radius please enter a number.")
# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
name = str(input("Enter your name:"))
while not name.strip() or name.isdigit() :
    print("Invalid input Please enter a valid name")
    name = input("Enter your name: ")
email = input("Enter your email:")
print(name)
print(email)
# # 	- Write a program that prints the number of times the substring 'iti' occurs in a string
string1 = str(input("Enter your string:"))
print(string1.count("iti"))