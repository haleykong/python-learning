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
# - A global and locally scoped versions of the variable can be created

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
