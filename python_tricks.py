# == FORMATTING ==
# SECTION SEPARATORS
print("=" * 79)
print("Test starting now...")

# PRINT NICE TABLES
import tabulate as tab

rows = [["myparam1", str(3.214)], ["myparam2", str(2.431)]]

print()
print('Tabular form:')
print(tab.tabulate(rows,
                   headers=["param", "value"],
                   tablefmt="fancy_grid"))

# ZIP/ENUMERATE/TABULATE
# 3rd party package imports
import tabulate as tab

print('-' * 79)
print('Example using zip:')
NAMES = ["Ky-Anh", "Haley", "Van-Anh"]
AGES = [32, 30, 33]
FOODS = ["kajiken", "boba", "macaron"]

for name, age, food in zip(NAMES, AGES, FOODS):
    print(f"{name}, {age}, {food}")

print('-' * 79)
print("Example using tabulate")
food_dict = {name: food for name, food in zip(NAMES, FOODS)}
age_dict = {name: age for name, age in zip(NAMES, AGES)}

rows = [["Person #", "Person Name", "Food", "age"]]
for ii, name in enumerate(NAMES):
    rows.append([f'{ii}', name, food_dict[name], age_dict[name]])
table = tab.tabulate(rows, headers='firstrow', tablefmt='fancy_grid')
print(table)

# PRINT NUMBERS WITH FIXED NUMBER OF SIGNIFICANT DIGITS
import numpy as np


def print_eng(num, sigfig=4):
    """Return a string of number formatted with engineering suffixes.

    Parameters
    ----------
    num: float
        Number to be printed
    sigfig: int
        Number of sig figs

    Returns
    -------
        Returns a string with nicely formatted scientific notation
        for example print_eng(1.2e-12) gives '1.200p'
    """
    if type(num) in [str]:
        return num
    SUFFIX = ['y', 'a', 'f', 'p', 'n', 'u', 'm', '', 'k', 'M', 'G', 'T']
    IDX_BASE = SUFFIX.index('')
    pos = abs(num)
    sgn = np.sign(num)
    # Compute the closest 3rd power of 10
    if num != 0:
        offset = int(np.log10(pos) // 3)
        val = sgn * pos / 10.0**(3 * offset)
        sfx = SUFFIX[offset + IDX_BASE]
        return f"{val:0.{sigfig}g}{sfx}"
    else:
        return "0.0"


print_eng(123456)

# == LOGGING ==
# LOGGING LEVELS
# standard imports
import logging

# 3rd party package imports
import consts

LOGGING_LVL = 3

logging.basicConfig(level=logging.INFO)

# Code
logging.info("This stuff only prints if level set to INFO or lower")
for ii in range(10):
    logging.info(consts.PASS)


# == OBJECTS ==
# OBJECT TYPE
example = []
type(example)

# == DUNDER ==
# __str__() function is a built-in function that returns a string for any
# python object.  That string is what python does when you do print(OBJECT)
sample = "hi"
sample.__str__()

# __dict__ attribute is a built-in attribute that provides a dictionary-like
# view of the class or instance namespace
class TempClass:
    a = 1
print(TempClass.__dict__)

