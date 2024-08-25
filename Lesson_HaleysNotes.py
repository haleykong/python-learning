# MEANING OF UNDERSCORES

# Single Leading Underscore
_var
# The underscore prefix is meant as a hint to another programmer that a
# variable or method starting with a single underscore is intended for internal
# use. This convention is defined in PEP 8.

# Single Trailing Underscore
var_
# A single trailing underscore (postfix) is used by convention to avoid naming
# conflicts with Python keywords. This convention is explained in PEP 8.

# Double Leading Underscore
__var
# A double underscore prefix causes the Python interpreter to rewrite the
# attribute name in order to avoid naming conflicts in subclasses.
# In name mangling process any identifier with two leading underscore and one
# trailing underscore is textually replaced with _classname__identifier where
# classname is the name of the current class. It means that any identifier of
# the form __geek (at least two leading underscores or at most one trailing
# underscore) is replaced with _classname__geek, where classname is the current
# class name with leading underscore(s) stripped.

# Double Leading and Trailing Underscore
__var__
# Name mangling is not applied if a name starts and ends with double
# underscores.
# Reserved for special use in the language
# This rule covers things like __init__ for object constructors, or
# __call__ to make an object callable.

# Single Underscore
_
# A single standalone underscore is sometimes used as a name to indicate that a
# variable is temporary or insignificant.
# ============================================================================
# STRING INTERPOLATION
# Link: https://realpython.com/python-f-strings/

# Option 1: The Modulo Operator, %
# >>> name = "Jane"
# >>> "Hello, %s!" % name
# 'Hello, Jane!'

# Option 2: The str.format() Method
# >>> name = "Jane"
# >>> age = 25
# >>> "Hello, {}! You're {} years old.".format(name, age)
# "Hello, Jane! You're 25 years old."

# Option 3: F-String
# >>> name = "Jane"
# >>> age = 25
# >>> f"Hello, {name}! You're {age} years old."
# 'Hello, Jane! You're 25 years old.'

# Corner Cases
# Passing by reference
d = [["C"] * 3] * 4
d[1][2] = 8
print(d)  # This will update all 2nd indices to 8
