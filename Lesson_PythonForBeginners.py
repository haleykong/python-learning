# -*- coding: utf-8 -*-
"""
Spyder Editor

This is my first python lesson.  The file will cover the following topics:
    - Basic Python functionality (If statements, For loops, While loops)
    - Basic Python data types (Lists, Numbers, Strings, Dictionaries, Tuples)
    
Tutorial Link: https://www.youtube.com/watch?v=rfscVS0vtbw
    
Additional resource and links (git repo )
"""
"""
# ------------------
# 1: DRAWING A SHAPE
# ------------------
# - Order of instructions matter
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("\n")

# ---------------------------
# 2: VARIABLES AND DATA TYPES
# ---------------------------
# - Variable is a container for a value
# - Names should be separated with an underscore
# - Datatypes: string, integer/number, boolean
character_name = "John"
character_age = "50"
is_male = True
print("There once was a man named " + character_name +  ", ")
print("he was " + character_age + " years old. ")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + character_age + ".")

print("\n")

# -----------------------
# 3: WORKING WITH STRINGS
# -----------------------
print("Giraffe Academy")
print("Giraffe\nAcademy") # New line
print("Giraffe\"Academy") # Quotation

# Concatenation is appending strings
phrase = "Giraffe Academy"
print(phrase + " is cool")

# Function = Block of code to perform specific operation
# - Used to modify strings or get info about string
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))

# Specify index of character
# String is indexed from 0
print(phrase[0]) 

# Passing a Parameter = Give a function a value
print(phrase.index("G")) # Search for location of string
print(phrase.replace("Giraffe", "Elephant"))

print("\n")

# -----------------------
# 4: WORKING WITH NUMBERS
# -----------------------
# Import math module
from math import *

print(3 * (4 + 5))
print(10 % 3) # Modulus operator; provides remainder after division

my_num = -5
print(str(my_num) + " is my favorite number") # Convert into string
print(abs(my_num)) # Absolute value
print(pow(3, 2)) # Number, power to take the number
print(max(4, 6)) # Returns the larger of the two numbers
print(min(4, 6)) # Returns the smaller of the two numbers
print(round(3.2)) # Rounds the number
print(floor(3.7)) # Rounds down
print(ceil(3.7)) # Rounds up
print(sqrt(36)) # Square root

print("\n")

# ---------------------------
# 5: GETTING INPUT FROM USERS
# ---------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

print("\n")

# ------------------------------
# 6: BUILDING A BASIC CALCULATOR
# ------------------------------
# By default, input is a string
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) # Convert from string to float

print(result)

print("\n")

# ----------------
# 7: MAD LIBS GAME
# ----------------
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

print("\n")

# --------
# 8: LISTS
# --------
# Lists = Structure to store lists of information (strings, numbers booleans)
# - Uses []
friends = ["Kevin", "Karen", "Jim"]

# Each element has an index (starts at 0)
print(friends[-1]) # Index from the back of the list
print(friends[1:]) # Elements after an index
print(friends[0:2]) # Elements in a range

# Edit element at index
friends[1] = "Mike"
print(friends[1]) 

print("\n")

# -----------------
# 9: LIST FUNCTIONS
# -----------------
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers) # Append a list
friends.append("Creed") # Append another item at the end of list

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly") # Insert element at index
friends.remove("Jim") # Remove an element

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop() # Remove last element

print(friends.index("Oscar")) # Determine index of element
print(friends.count("Jim")) # Count nummber of occurrences
friends.sort() # Sort in alphabetical/ascending order
lucky_numbers.reverse() # Sort in reverse order
print(friends)

friends2 = friends.copy() # Copy a list
print(friends2)

friends.clear() # Remove everything in list
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]

print(lucky_numbers[3] == 16)
print(lucky_numbers[2:4])
print(23 in lucky_numbers)

# You can append lists
numbers1 = [1, 2, 3]
numbers2 = [3, 4, 5, 6]
numbers3 = numbers1 + numbers2
print(numbers3)

print("\n")

# ----------
# 10: TUPLES
# ----------
# Tuples = Data structure that is a container that can store different values
# - Uses ()
# - Immutable (this is what is different from a list)
# - Indexed at 0
# Tuples are a sequence data type with immutable values in Python. 
# Commas separate the values in a tuple.

coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[0])

print("\n")

# ------------
# 11: FUNCTION
# ------------
# Function = Collection of code that performs a specific task
# - Helpful for organizing code
# - Code that goes inside the function needs to be indented
# - Functions should be all lowercase
# Parameter = Information that you give to a parameter
# A block of code that is executed when it is called is defined as a function. 
# The keyword def is used to define a Python function.

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))
    
say_hi("Mike", 35) # Call the function
say_hi("Steve", 70)

print("\n")

# --------------------
# 12: RETURN STATEMENT
# --------------------
# Return = Returns information from function and breaks out of function
def cube(num):
    return num * num * num 

result = cube(4)
print(result)

print("\n")

# -----------------
# 13: IF STATEMENTS
# -----------------
# - Execute code depending on input
# - Condition is either true or false
# - and operator | or operator
is_male = True
is_tall = False

if is_male and is_tall: 
    print("You are tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print ("You are not a male and not tall")
    
print("\n")

# -------------------------------
# 14: IF STATEMENTS & COMPARISONS
# -------------------------------
# - Comparisons will result in a True or False
# - Can compare numbers or strings
# - Comparison Operators: ==, !=, >, <, <=, >=
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3, 4, 5))

print("\n")

# --------------------------------
# 15: BUILDING A BETTER CALCULATOR
# --------------------------------
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print (num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")

print("\n")

# ----------------
# 16: DICTIONARIES
# ----------------
# Dictionary = Structure that can store key-value pairs
# - Uses {}
# - Keys can be strings or numbers
monthConversions = {
    "Jan": "January",
    "Feb": "February", 
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Luv", "Not a valid key")) # Can specify a default value if key is not found

print("\n")

# --------------
# 17: WHILE LOOP
# --------------
# While Loop = Structure that can execute block of code multiple times
# - Contains loop condition or loop guard
i = 1
while i <= 10:
    print(i)
    i += 1
    
print("Done with loop")

print("\n")

# ----------------------------
# 18: BUILDING A GUESSING GAME
# ----------------------------
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:    
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
    
print("\n")

# ------------
# 19: FOR LOOP
# ------------
# - Define a variable
# - Variable changes with each iteration of the loop
# Looping through each letter in the string
for letter in "Giraffe Academy": 
    print(letter)

# Looping through each element in the array
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
    
len(friends)
for index in range(len(friends)):
    print(friends[index])
    
# Looping through numbers
for index in range(3, 10):
    print(index)
    
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")
        
print("\n")

# ---------------------
# 20: EXPONENT FUNCTION
# ---------------------
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))

print("\n")

# ---------------------------
# 21: 2D LISTS & NESTED LOOPS
# ---------------------------
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]    
]

for row in number_grid:
    for col in row:
        print(col)

print("\n")

# ----------------------
# 22: BUILD A TRANSLATOR
# ----------------------
# vowels -> g
# dog -> dgg
# cat -> cgt
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

print("\n")

# ------------
# 23: COMMENTS
# ------------
# Comment = Not rendered by Python, used by developers to make notes
# Single-line comment
# ''' Multi-line comment '''

print("\n")

# ----------------
# 24: TRY / EXCEPT
# ----------------
# - Catch specific errors and do things when they occur
# - Best practice is to except for a specific error
try: 
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # Store error as variable
    print(err)
except ValueError:
    print("Invalid Input")
    
print("\n")

# -----------------
# 25: READING FILES
# -----------------
# - Read from files outside of Python file
# - r is read, w is write, a is append, r+ is read and write
# - Need to both open and close a file
employee_file = open("employees.txt", "r") # Exists in same directory, also state the mode to open the file in

print(employee_file.readable()) # Checks whether we can read from the file

for employee in employee_file.readlines():
    print(employee)
    
employee_file.close()

print("\n")

# --------------------
# 26: WRITING TO FILES
# --------------------
# - w overwrites everything in the file, can be used to create a new file
employee_file = open("employees.txt", "w")

employee_file.write("\nKelly - Customer Service")

employee_file.close()

print("\n")

# -------------------
# 27: MODULES AND PIP
# -------------------
# Module = External Python file that you can import into current Python file
# - Built-In Modules = part of the Python language
# - External Modules = stored inside the Lib folder (part of Python downloads)
# - Downloaded Modules = under site-packages 
# pip = program to install Python modules (package manager),comes with Python 3
import useful_tools # Grabs the content in useful_tools.py

print(useful_tools.roll_dice(10))

print("\n")

# -----------------------
# 28: CLASSES AND OBJECTS
# -----------------------
# Class = define new datatype (e.g. what is a Student)
# Object = instance of Class (e.g. a Student)
from Student import Student # From Student file, import Student class

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student2.gpa)

print("\n")

# -----------------------------------
# 29: BUILDING A MULTIPLE CHOICE QUIZ
# -----------------------------------
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)

print("\n")

# -----------------------------------
# 29: BUILDING A MULTIPLE CHOICE QUIZ
# -----------------------------------
# Class Function = Function used inside of a class that help user to figure out 
# info about the object or modify different values in object
from Student import Student

student1 = Student("Oscar","Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())

print("\n")

# ---------------
# 30: INHERITANCE
# ---------------
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

print("\n")

# ----------------------
# 31: PYTHON INTERPRETER
# ----------------------
# Python Interpreter = Environment to execute Python commands
# In Terminal, you can type python3
