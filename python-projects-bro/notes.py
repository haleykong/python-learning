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
#
# FUNCTION ASSIGNMENT TO VARIABLES


def hello():
    print("Hello")


hi = hello  # Get memory address from hello and set it to hi
hello()
hi()

say = print
say("Whoa! I can't believe this works! :O")

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

###############################################################################
# OBJECT-ORIENTED PROGRAMMING
#
# OBJECT = instance of a class
# CLASS = describes attributes and methods (like a blueprint)
# - Class should be capitalized, can be in main module or separate file
# ATTRIBUTE = what an object is/has
# METHOD = what an object can do
#
# INSTANCE VARIABLE = declared inside instructor and each object can have
# unique values assigned
# CLASS VARIABLE = declared inside of class but outside constructor


class Car:
    # Class variables
    wheels = 4

    # Special method that will construct objects
    # Also called the Constructor
    def __init__(self, make, model, year, color):
        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable

    # Self = object that is using this method
    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")


car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_1.drive()
car_1.stop()
car_1.wheels
Car.wheels = 2  # Affects all instances of the class

###############################################################################
# INHERITANCE
#
# - Classes can have children
# - Parent-child relationship where children will inherit from the parents
# (attributes and methods)
# - Children classes can implement their own unique attributes and methods


class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


# Rabbit is the child class, Animal is the parent class
class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")


class Fish(Animal):

    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()

###############################################################################
# MULTI-LEVEL INHERITANCE
#
# MULTI-LEVEL INHERITANCE = when a derived (child) class inherits another
# derived (child) class


class Organism:

    alive = True


class Animal(Organism):

    def eat(self):
        print("This animal is eating")


class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)    # inherited from the Organism class
dog.eat()           # inherited from the Animal class
dog.bark()          # defined in Dog class

###############################################################################
# MULTIPLE INHERITANCE
#
# MULTIPLE INHERITANCE = when a child is derived from more than 1 parent class


class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()

###############################################################################
# METHOD OVERRIDING
#
# METHOD OVERRIDING - child class provides a specific implementation of a
# method that is already provided by one of its parent
# - Object will use method that is more closely associated with itself


class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):

    # Same method signature as Animal class
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()

###############################################################################
# METHOD CHAINING
#
# METHOD CHAINING - calling multiple methods sequentially
# - Each call performs an action on the same object and returns self


class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()
# Notation 1
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
# Notation 2
car.turn_on().drive().brake().turn_off()

###############################################################################
# SUPER FUNCTION
#
# super() = Function used to give access to the methods of a parent class
# - Returns a temporary object of a parent class when used


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        # Use the init function from Rectangle class
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        # Use the init function from Rectangle class
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

###############################################################################
# ABSTRACT CLASSES
#
# ABSTRACT CLASS = a class which contains one or more abstract methods
# - prevents a user from creating an object of that class
# - Compels a user to override abstract methods in a child class
# ABSTRACT METHOD = a method that has a declaration but does not have an
# implementation


from abc import ABC, abstractmethod  # Abstract Base Class


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()  # Causes an error because Vehicle is an Abstract Class
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

###############################################################################
# OBJECTS AS ARGUMENTS
#
# - Can pass objects as args to function like with variables
# - Type of objects may be limited based on required attributes or methods


class Car:

    color = None


class Motorcycle:

    color = None


def change_color(car, color):
    car.color = color


car_1 = Car()
bike_1 = Motorcycle()

change_color(car_1, "red")
change_color(bike_1, "black")

print(car_1.color)
print(bike_1.color)

###############################################################################
# DUCK TYPING
#
# DUCK TYPING = concept where the class of an object is less important than the
# methods/attributes it might have
# - Class type is not checked if minimum methods/attributes are present
# - Based off of the phrase: "If it walks like a duck, and it quacks like a
# duck, then it must be a duck"


class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)

###############################################################################
# WALRUS OPERATOR :=
#
# WALRUS OPERATOR = assigns values to variables as part of a larger expression
# - Assignment expression
# - New to Python 3.8


print(happy := True)

# Without walrus operator
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

# With walrus operator
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

###############################################################################
# HIGHER ORDER FUNCTION
#
# HIGHER ORDER FUNCTION = a function that either:
# 1. Accepts a function as an argument or
# 2. Returns a function (In python, functions are also treated as objects)

# Example of 1)


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)

# Example of 2)


def divisor(x):  # Returns the dividend function
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))

###############################################################################
# LAMBDA FUNCTIONS
#
# LAMBDA FUNCTION = function written in 1 line using lambda keyword
# - Accepts any number of arguments, but only has one expression
# - Useful if needed for a short period of time, throw-away
# lambda parameters:expression

# Without lambda


def double(x):
    return x * 2


print(double(5))

double = lambda x: x * 2
multiple = lambda x, y: x * y
add = lambda x, y, z: x + y + z
print(double(5))

###############################################################################
# SORT FUNCTIONS
#
# sort() method     = used with lists
# sorted() function = used with iterables
# - Can pass in keyword arguments: key and reverse

students = ("Squidward", "Sandy", "Patrick")

students.sort(reverse=True)
sorted_students = sorted(students, reverse=True)

###############################################################################
# MAP
#
# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function, iterable)


store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1] / 0.82)

store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)

###############################################################################
# FILTER
#
# filter() = creates a collection of elements from an iterable for which a
# function returns true
#
# filter(function, iterable)


friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)

###############################################################################
# REDUCE
#
# reduce() = apply a function to an iterable and reduce it to a single
# cumulative value
# - Performs function on first two elements and repeats process until 1 value
# remains
#
# reduce(function, iterable)


import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)

###############################################################################
# LIST COMPREHENSION
#
# LIST COMPREHENSION = a way to create a new list with less syntax
# - Can mimic certain lambda functions, easier to read
#
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression (if/else) for item in iterable]


# No list comprehension
squares = []                # create an empty list
for i in range(1, 11):      # create a for loop
    squares.append(i * i)   # define what each loop iteration should do
print(squares)

# List comprehension (example 1)
squares = [i * i for i in range(1, 11)]
print(squares)

# List comprehension (example 2)
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = [i for i in students if i >= 60]
passed_students2 = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)
print(passed_students2)

###############################################################################
# DICTIONARY COMPREHENSION
#
# DICTIONARY COMPREHENSION = create dictionaries using an expression
# - Can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

# Example 1
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5 / 9))
               for (key, value) in cities_in_F.items()}
print(cities_in_C)

# Example 2
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny"}
sunny_weather = {key: value for (key, value) in weather.items()
                 if value == "sunny"}
print(sunny_weather)

# Example 3
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value)
               in cities.items()}
print(desc_cities)


# Example 4
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)

###############################################################################
# ZIP
#
# zip(*iterables) = aggregate elements from two or more iterables (list,
# tuples, sets, etc.)
# - Creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = zip(usernames, passwords)

print(type(users))
for i in users:
    print(i)

###############################################################################
# IF __NAME__
#
# if __name__ == '__main__'
#
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules
#
# - Python interpreter sets "special variables", one of which is __name__
# - Python will assign the __name__ variable a value of '__main__' if it's the
# initial module being run
# - Checks to see if the file is being run directly or indirectly

import module_two
print(__name__)             # prints __main__
print(module_two.__name__)  # prints module_two

###############################################################################
# TIME MODULE
#
# epoch = a date and time from which a computer measures system time (when
# your computer thinks time began)
# UTC = Coordinated Universal Time
# - Primary time standard by which the world regulates clocks and times
# - Within about 1 second of mean solar time at 0 degrees longitude
# - Not adjusted for daylight savings time

import time

# Converts a time expressed in seconds since epoch to a readable string
print(time.ctime(0))
print(time.time())              # return current seconds since epoch
print(time.ctime(time.time()))  # get current date and time

time_object = time.localtime()      # create time object with epoch
time_object_utc = time.gmtime()     # create time object with UTC time
# use different directives to change formats
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)

time_string = "20 April, 2020"
# parses a string representation of time or date and returns a time object
time_object = time.strptime(time_string, "%d %B, %Y")

# (year, month, day, hours, minutes, secs, #day of the wk, #day of the yr, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# takes a time object or a tuple representation
time_string = time.asctime(time_tuple)
print(time_string)

###############################################################################
# THREADING
#
# thread = a flow of execution, like a separate order of instructions
# - Each thread takes a turn running to achieve concurrency
# - GIL = Global Interpreter Lock, allows only one thread to hold the control
# of the Python interpreter at any one time
#
# CPU bound = program/task spends most of its time waiting for internal events
# (CPU intensive)
# - Use multiprocessing
#
# IO bound = program/task spends most of its time waiting for external events
# (user input, web scraping)
# - Use multithreading (multiple threads using concurrently)


import threading
import time


# IO bound because waiting for sleep
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


# IO bound because waiting for sleep
def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


# IO bound because waiting for sleep
def study():
    time.sleep(5)
    print("You finish studying")


# Create additional threads and now can run each task concurrently
# Main thread creates this
x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

# Main thread needs to wait until these threads synchronize
x.join()
y.join()
z.join()

# Main thread
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

###############################################################################
# DAEMON THREAD
#
# DAEMON THREAD = a thread that runs in the background
# - Not important for a program to run
# - Program will not wait for daemon threads to complete before exiting
# - Non-daemon threads cannot normally be killed, they stay alive until task is
# complete
#
# (e.g. background tasks, garbage collection, waiting for input, long-running
# processes)


import threading
import time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.setDaemon(True)  # Another way to set if daemon
x.start()


answer = input("Do you wish to exit?")

###############################################################################
# MULTIPROCESSING
#
# MULTIPROCESSING - running tasks in parallel on different CPU cores
# - Bypass GIL used for threading
# - Multiprocessing - better for CPU bound tasks (heavy CPU usage)
# - Multithreading - better for IO bound tasks (waiting around)


from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in:", time.perf_counter(), "seconds")


# Throws an error because bug requires module to be imported for multiprocess
if __name__ == '__main__':
    main()

###############################################################################
# AUTOMATED EMAILS


import smtplib  # Simple Mail Transfer Protocol Library


sender = "sender@gmail.com"         # Placholder
receiver = "receiver@gmail.com"     # Placeholder
password = "password123"            # Placeholder
subject = "Python email test"
body = "I wrote an email! :D"

message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage {receiver}
Subject: {subject}\n
{body}
"""

# 587 = default mail submission port
server = smtplib.SMTP("smtp.gmail.com", 587)
# TLS = Transport layer security
server.starttls()

try:
    server.login(sender, password)
    print("Logged in")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")

