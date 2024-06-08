#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:46:01 2023

@author: haleykong
"""

# NOTES:
# Can modify variables for a Class (Person) or an instance of the Class/object


class Person:
    class_variable = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.nodes = 1
        self.info = name+"s age is "+str(age)
        print('-' * 79)
        print('name = %s' % name)
        print("Random string i printed while creating this object")


# person1 = Person('ky-anh', 31)
# person2 = Person('haley', 30)

list_of_persons = []

for ii in range(30):
    list_of_persons.append(Person('blahblah %s' % ii, ii))


for jj in range(10):
    list_of_persons[0].class_variable += 1

print(list_of_persons[1].class_variable)

# =============================================================================
# NOTES: Need to have arguments passed in UNLESS it's defined in the definition


def example_fn_with_optional_arg(a, b=1, c=1):
    return a + 2*b + 2*c
