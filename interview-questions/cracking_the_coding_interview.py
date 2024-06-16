# 1.1 Is Unique - Determine if a string has all unique characters
#
# Check - Is this an ASCII string or a Unicode string?

def is_unique(str):
    # Assume the character set is ASCII
    if len(str) > 128: return False

    frequency = {}
    for char in str:
        if char in frequency:
            return False
        else:
            frequency[char] = 1
    return True

# Time Complexity: O(n) or O(c) where c is the size of the character set
# Space Complexity: O(1)


# 1.2 Check Permutation - Given two strings, write a method to decide if one
# is a permutation of the other
#
# Check - Is the permutation comparison case-sensitive? Is whitespace
# significant? What is the size of the character set?

def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    frequency1 = {}
    frequency2 = {}

    for char in string1:
        if char not in frequency1:
            frequency1[char] = 1
        else:
            frequency1[char] += 1

    for char in string2:
        if char not in frequency2:
            frequency2[char] = 1
        else:
            frequency2[char] += 1

    return frequency1 == frequency2


# 1.3 URLify - Write a method to replace all spaces in a string with "%20"

def urlify(str):
    url = ""
    for char in str:
        if char == " ":
            url += "%20"
        else:
            url += char
    return url


# 1.4 Palindrome Permutation - Given a string, write a function to check if it
# is a permutation of a palindrome

def palindrome_permutation(input_string):
    input_string = input_string.lower().replace(" ", "")
    print(input_string)

    # Determine character count of input string
    frequency = {}
    for char in input_string.strip():
        if char == " ":
            continue
        elif char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    print(frequency)
    return check_max_one_odd(frequency)


def check_max_one_odd(frequency):
    found_odd = False
    for char, count in frequency.items():
        if (count % 2 == 1):
            if found_odd:
                return False
            else:
                found_odd = True
    return True

# Time Complexity: O(N) where N is the length of thes string


# 1.5 One Away - There are three types of edits that can be performed on
strings: insert a character, remove a 
# TEST CODE BELOW
print(palindrome_permutation("abza"))