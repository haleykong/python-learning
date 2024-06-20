###############################################################################
# VARIABLES
#
# VARIABLE = container for a value. Behaves as the value it contains.
# - STRING = series of characters
# - INTEGER = a whole number
# - FLOAT = floating point number (a decimal number)
# - BOOLEAN = true or false

# SCOPE = the region that a variable is recognized
# - A variable is only available from inside the region it is created
# - Local scope = available only inside the function
# - Global scope = available inside and outside the function

###############################################################################
# MULTIPLE ASSIGNMENT
#
# MULTIPLE ASSIGNMENT = Allows us to assign multiple variables at the same
# in one line of code

Spongebob, Patrick, Sandy, Squidward = 30

###############################################################################
# STRING METHODS

name = "Bro Code"
len(name)  # Determines length of string
name.find("o")  # Find character within string
name.capitalize()  # Capitalizes first letter of string
name.upper()  # Entire string is uppercase
name.lower()  # Enter string is lowercase
name.isdigit()  # Returns if string is a digit
name.isalpha()  # Returns if string is all letters
name.count("o")  # Counts the number of times the characters appear in string
name.replace("o", "a")  # Replaces first string with second
name * 3  # Displays the string the number of times as the multiplier

###############################################################################
# TYPE CASTING
#
# TYPE CASTING = convert the data type of a value to another data type
x = 1.0
int(x)
float(x)
str(x)

###############################################################################
# USER INPUT
#
# - User input always returns as a string
input("prompt")

###############################################################################
# MATH FUNCTIONS
#
import math

pi = 3.14

round(pi)  # Round the number
math.ceil(pi)  # Round the number up
math.floor(pi)  # Round the number down
abs(pi)  # Absolute value of a number
pow(pi, 2)  # Raise a base number to a power
math.sqrt(pi)  # Square root of a number
max()  # Find the largest value
min()  # Find the lowest value

###############################################################################
# STRING SLICING
#
# SLICING = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

website = "http://google.com"

slice = slice(7, -4)
website[slice]

###############################################################################
# - IF STATEMENT = a block of code that will execute if its condition is true

# - LOGICAL OPERATORS (and, or, not) = used to check if two or more conditional
# statements are true

# - WHILE LOOP = a statement that will execute its block of code, as long as
# its condition remains true

# - FOR LOOP = a statement that will execute its block of code a limited amount
# of times

# - NESTED LOOP = the "inner loop" will finish all of its iterations before
# finishing one iteration of the "outer loop"

###############################################################################
# LOOP CONTROL
#
# LOOP CONTROL STATEMENTS = change a loop's execution from its normal sequence
# - break = used to terminate the loop entirely
# - continue = skips to the next iteration of the loop
# - pass = does nothing, acts as a placeholder

###############################################################################
# LISTS
#
# LIST = used to store multiple items in a single variable
food = ["pizza", "hamburger"]
food.append("ice cream")  # Add an element
food.remove("hot dog")  # Remove an element
food.pop()  # Remove last element
food.insert(0, "cake")  # Insert at a certain index
food.sort()  # Sort
food.clear()  # Clear

###############################################################################
# TUPLE
#
# TUPLE = collection which is ordered and unchangeable
# - Used to group together related data
student = ("Bro", 21, "male")
student.count("Bro")  # Count how many times the input appears
student.index("male")  # Returns index of value

###############################################################################
# SET
#
# SET = collection which is unordered and index. No duplicate values
# - Faster than a list
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}
utensils.add("napkin")  # Add an element
utensils.remove("fork")  # Remove an element
utensils.clear()  # Remove all elements of set
utensils.update(dishes)  # Add one set to the other
dinner_table = utensils.union(dishes)  # Create a new set from two sets
# Determine what is in the first set that is not in the second
utensils.difference(dishes)
# Determines which elements two sets have in common
utensils.intersection(dishes)

###############################################################################
# DICTIONARIES
#
# DICTIONARY = a changeable, unordered collection of unique key:value pairs
# - Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing'}
capitals.get('Germany')  # Check if key is in dictionary
capitals.keys()  # Returns all keys
capitals.values()  # Returns only values
capitals.items()  # Returns all key-value pairs
capitals.update({'Germany': 'Berlin'})  # Add to/update the dictionary
capitals.pop('China')  # Remove the specified key-value pair
capitals.clear()  # Clear the dictionary

###############################################################################
# FUNCTIONS
#
# FUNCTION = a block of code which is executed only when it is called
# ARGUMENT = information that is sent to a function
# PARAMETER = information that is used in a function
#
# RETURN STATEMENT = functions send Python values/objects back to the caller.
# These values/objects are known as the function's return value.

###############################################################################
# KEYWORD ARGUMENTS
#
# KEYWORD ARGUMENTS = arguments preceded by an identifier when we pass them to
# a function. The order of the arguments doesn't matter, unlike positional
# arguments, Python knows the names of the arguments that our function receives


def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="Code", middle="Dude", first="Bro")

###############################################################################
# ARGS
#
# *args = parameter that will pack all arguments into a tuple
# - Useful so that a function can accept a varying amount of positional
# arguments
#
# **kwargs = parameter that will pack all arguments into a dictionary
# - useful so that a function can accept a varying amount of keyword arguments


def add(*args):
    sum = 0
    for i in args:
        sum += 1
    return sum


def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])


print(add(1, 2, 3, 4, 5))
print(hello(first="Bro", middle="Dude", last="Code"))

###############################################################################
# STRING FORMAT
#
# str.format() = optional method that gives users more control when displaying
# output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))  # positional arg
print("The {item} jumped over the {animal}".format(animal="cow", item="moon"))

# PADDING
name = "Bro"

print("Hello, my name is {:10}. Nice to meet you".format(name))

# Left align within padding
print("Hello, my name is {:<10}. Nice to meet you".format(name))

# Right align within padding
print("Hello, my name is {:>10}. Nice to meet you".format(name))

# Center align within padding
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 1000

# Truncate and round to the number digits specified
print("The number is {:.3f}".format(number))

# Add comment to all 1000th places
print("The number is {:,}".format(number))

# Display binary representation
print("The number is {:b}".format(number))

# Display octal representation
print("The number is {:o}".format(number))

# Display hexidecimal representation
print("The number is {:x}".format(number))  # lowercase
print("The number is {:X}".format(number))  # uppercase

# Display in scientific notation
print("The number is {:e}".format(number))  # lowercase
print("The number is {:E}".format(number))  # uppercase

###############################################################################
# RANDOM MODULE
#
import random

x = random.randint(1, 6)  # Generate random integer
y = random.random()  # Generate random float

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)  # Generates random choice from list
random.shuffle(myList)  # Shuffle the list

###############################################################################
# EXCEPTION HANDLING
#
# EXCEPTION - events deteected during execution that interrupt the flow of a
# program
# - Not good practice to have single except block to handle all exceptions
# - Better to handle individual exceptions

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)  # Print exception
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:  # General exceptions
    print(e)
    print("Something went wrong :(")
else:  # If no exception
    print(result)
finally:  # Regardless of if there was an exception
    print("This will always execute")

###############################################################################
# FILES
#
import os  # Included in standard Python library

path = "/Users/haleykong/TEST"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")

# READ A FILE
try:
    # Closes a file but does not handle errors
    with open('/Users/haleykong/TEST') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

print(file.closed)  # Check if file is closed

# ----------------------------------------------------------------------------
# WRITE A FILE
# r = read mode
# w = write mode
# a = append mode
text = "Yooooo\nThis is some text\nHave a good one!\n"

with open('/Users/haleykong/TEST', 'w') as file:
    file.write(text)

# ----------------------------------------------------------------------------
# COPY A FILE
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
import shutil

shutil.copyfile('/Users/haleykong/TEST', '/Users/haleykong/TEST1')  # src, dest

# ----------------------------------------------------------------------------
# MOVE A FILE
import os

source = ""
destination = ""

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

# ----------------------------------------------------------------------------
# DELETE A FILE
import os
import shutil

path = "/Users/haleykong/TEST"

try:
    os.remove(path)  # Deletes a file, does not remove folders
    os.rmdir(path)  # Deletes an empty directory
    shutil.rmtree(path)  # Deletes a directory and all files that it contains
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")

###############################################################################
# MODULES
#
# MODULE = a file containing python code
# - May contain functions, classes, etc.
# - Used with modular programming, which is to separate a program into parts
# Example 1)
# import messages as msg
# msg.hello()
# Example 2)
# from messages import hello, bye
# hello()  # Can call directly
help("modules")  # Prints available modules
