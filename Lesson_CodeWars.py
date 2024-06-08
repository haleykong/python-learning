# PROBLEM: Grasshopper - Summation
# Write a program that finds the summation of every number from 1 to num.

# SOLUTION:
def summation(num):
    return sum(range(num + 1))

# TAKEAWAYS:
# sum() function adds the items of an iterable and returns the sum
# range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1, and ends at a specified number

# =============================================================================

# PROBLEM: Is it a number?
# Given a string s, write a method (function) that will return true if its a
# valid single integer or floating number or false if its not.
# EXAMPLE:
# isDigit("  3  ") == True
# isDigit("  3   5") == False

# SOLUTION:


def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False

# TAKEAWAYS:
# try block lets you test a block of code for errors
# except block lets you handle the error

# =============================================================================

# PROBLEM: A Letter's Best Friend
# Given a string, return if a given letter always appears immediately before
# another given letter.
# EXAMPLE:
# ("he headed to the store", "h", "e") ➞ True
# ('abcdee', 'e', 'e') ➞ False

# SOLUTION:


def best_friend(txt, a, b):
	return txt.count(a) == txt.count(a + b)

# TAKEAWAYS:
# - Count() counts the number of occurrences of a specified substring in the
# string. count(a + b) counts the number of times the concatenated string a + b
# appears

# =============================================================================

# PROBLEM: Add Length
# Write a function that takes a String and returns an Array/list with the
# length of each word added to each element.
# EXAMPLE:
# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]

# SOLUTION:


def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]

# TAKEAWAYS:
# - List Comprehension
# =============================================================================

# PROBLEM: Gravity Flip
# - Given the initial configuration of the cubes in the box, find out how many
# cubes are in each of the n columns after Bob switches the gravity.
# EXAMPLE:
# * 'R', [3, 2, 1, 2]      ->  [1, 2, 2, 3]
# * 'L', [1, 4, 5, 3, 5 ]  ->  [5, 5, 4, 3, 1]

# SOLUTION:


def flip(d, a):
    return sorted(a, reverse=d == 'L')

# TAKEAWAYS:
# The simplest difference between sort() and sorted() is: sort() changes the
# list directly and doesn't return any value, while sorted() doesn't change the
# list and returns the sorted list
# =============================================================================

# PROBLEM: Finish Guess the Number Game
# - If the user tries to guess more than the limit, the function should throw
#   an error
# - If the user guess is right it should return true
# - If the user guess is wrong it should return false and lose a life

# SOLUTION:


class Guesser:
  def __init__(self, number, lives):
    self.number = number
    self.lives = lives

  def guess(self, n):
    if self.lives < 1: raise "Too many guesses!"
    if self.number == n: return True
    self.lives -= 1
    return False

# TAKEAWAYS:
# - raise = Throws or raises an exception if a condition occurs
# =============================================================================
# PROBLEM: Playing with cubes II
# - Create a constructor. The constructor takes no arguments should assign 0 to
#   Cube's Side property
# - Correct the code so negative values will be switched to positive ones!

# SOLUTION:


class Cube:
    def __init__(self, side=0):
		self._side = abs(side)

	def get_side(self):
		"""Return the side of the Cube"""
		return self._side
	
	def set_side(self, new_side):
		"""Set the value of the Cube's side."""
		self._side = abs(new_side)
        
# TAKEAWAYS:
# - Leading underscore (_var) shows that the variable is for internal use
#   It is ignored by the interpreter.
# - Set the arg to default in the constructor, which makes it optional when 
#   using the constructor
# =============================================================================
# PROBLEM: OOP:Object Oriented Piracy
# - Each crew member adds 1.5 units to the ship draft
# - If after removing the weight of the crew, the draft is still more than 20,
#   then the ship is worth looting.

# SOLUTION:

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20

# TAKEAWAYS:
# - Self represents the instance of the class
# - By using the “self”  we can access the attributes and methods of the class
#   in Python. It binds the attributes with the given arguments
# - The reason you need to use self. is because Python does not use the
#   @ syntax to refer to instance attributes
# =============================================================================
# PROBLEM: Classy Extensions
# - Your task is to complete the Cat class which Extends Animal and replace the
#   speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'

# SOLUTION:


class Cat(Animal):
    def speak(self):
        return self.name + ' meows.'

# TAKEAWAYS:
# - Inheritance
# =============================================================================
# PROBLEM: Color Ghost
# - Create a class Ghost
# - Ghost objects are instantiated without any arguments
# - Ghost objects are given a random color attribute of "white" or "yellow" or
# "purple" or "red" when instantiated

# SOLUTION:
# import random


class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# TAKEAWAYS:
# - Random = Built-in Python module that you can use to make random numbers
# - choice() method returns a randomly selected element from the specified
#   sequence. The sequence can be a string, a range, a list, a tuple or any
#   other kind of sequence
# =============================================================================
# PROBLEM: Classy Classes
# - You must fill in the Constructor method to accept a name as string and an
# age as number, complete the get Info property and getInfo method/Info getter
# which should return johns age is 34

# SOLUTION:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return '{}s age is {}'.format(self.name, self.age)

# TAKEAWAYS:
# - @ is a decorator that allows you to augment a function
# - @property adds managed attributes to a class. Allows get/set/delete of
# =============================================================================


# PROBLEM: Find the unique number
# - There is an array with some numbers
# - All numbers are equal except for one
# EXAMPLE:
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2

# SOLUTION:


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

# TAKEAWAYS:
# - Set is one of 4 built-in data types in Python used to store collections of
#   data. The other 3 are List, Tuple, and Dictionary. Sets are used to store
#   multiple items in a single variable
# - A set is a collection which is unordered, unchangeable, and unindexed.
#   Once a set is created, you cannot change its items, but you can remove
#   items and add new items.
# - Assign variables to different indices of the set
# =============================================================================

# PROBLEM: Find the next perfect square!
# - Complete the findNextSquare method that finds the next integral perfect
#   square after the one passed as a parameter. Recall that an integral perfect
#   square is an integer n such that sqrt(n) is also an integer.
# - If the parameter is itself not a perfect square then - 1 should be
#   returned. You may assume the parameter is non-negative.
# EXAMPLE:
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

# SOLUTION:


def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

# TAKEAWAYS:
# - ** is exponentiation operator
# =============================================================================

# PROBLEM: Exes and Ohs
# - Check to see if a string has the same amount of 'x's and 'o's
# - The method must return a boolean and be case insensitive
# - The string can contain any char
# EXAMPLE:
# xo("ooxx") => true
# xo("xooxx") => false

# SOLUTION:


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# TAKEAWAYS:
# The count() method returns the number of elements with the specified value
# =============================================================================

# PROBLEM: Find The Parity Outlier
# - The array is either entirely comprised of odd integers or entirely
#   comprised of even integers except for a single integer N
# - Write a method that takes the array as an argument & returns "outlier" N
# EXAMPLE:
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

# SOLUTION:

    def find_outlier(int):
        odds = [x for x in int if x % 2 != 0]
        evens = [x for x in int if x % 2 == 0]
        return odds[0] if len(odds) < len(evens) else evens[0]

# TAKEAWAYS:
# - List Comprehension
# - newlist = [expression for item in iterable if condition == True]
# =============================================================================

# PROBLEM: Who likes it?
# - Implement the function which takes an array containing the names of people
#   that like an item
# EXAMPLE:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# SOLUTION:


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

# TAKEAWAYS:
# - The format() method formats the specified value(s) and inserts them inside
#   the string's placeholder.
# - * initializes a Tuple
# - names[:3] is a list (names) that contains all elements up to the 3rd one

# =============================================================================

# PROBLEM: Leap Years
# - Determine whether a given year is a leap year or not
# - Years divisible by 4 are leap years
# - Years divisible by 100 are not leap years
# - Years divisible by 400 are leap years.

# SOLUTION:


def is_leap_year(year):
    return (year % 100 and not year % 4) or not year % 400


isLeapYear = is_leap_year

# TAKEAWAYS:
# - Return statements for conditions
# =============================================================================
