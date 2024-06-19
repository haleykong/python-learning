###############################################################################
# VARIABLES
#
# VARIABLE = container for a value. Behaves as the value it contains.
# - STRING = series of characters
# - INTEGER = a whole number
# - FLOAT = floating point number (a decimal number)
# - BOOLEAN = true or false

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
