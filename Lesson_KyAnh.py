# PYTHON LIST
# Python list comprehension allows you to create lists that have
# structure to them in a colloquial way

# For example, to create a list of numbers like
# 1, 2^2, 3^2, 4^2, .... n^2

# In python you can do it 2 ways:
# METHOD 1: For loop with conditional test

x1 = []
n = 50
for i in range(n):
    x1.append(i**2)

# METHOD 2:List Comprehension
# Using list comprehension, it's much shorter:
x2 = [ii**2 for ii in range(n)]

# note ii here is a dummy variable used to explain what we do with 
# element "ii"    

# STRING MANIPULAITION
# String multiplication
a = 'skjdldakfj'
delimiter = '=' * 79
print(delimiter)

# String contains
b = 's' in a
print(b)

a = [5, 5, 5, 5, 1, 5, 5]
b = set(a)

c, d = b


a, b = ('a' , 'b')