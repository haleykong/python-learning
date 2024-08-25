###############################################################################
# 1.1 IS UNIQUE - Determine if a string has all unique characters
#
# Check - Is this an ASCII string or a Unicode string?

def is_unique(str):
    # Assume the character set is ASCII
    if len(str) > 128:
        return False

    frequency = {}
    for char in str:
        if char in frequency:
            return False
        else:
            frequency[char] = 1
    return True

# Time Complexity: O(n) or O(c) where c is the size of the character set
# Space Complexity: O(1)

###############################################################################
# 1.2 CHECK PERMUTATION - Given two strings, write a method to decide if one
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


###############################################################################
# 1.3 URLIFY - Write a method to replace all spaces in a string with "%20"

def urlify(str):
    url = ""
    for char in str:
        if char == " ":
            url += "%20"
        else:
            url += char
    return url


###############################################################################
# 1.4 PALINDROME PERMUTATION - Given a string, write a function to check if it
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


###############################################################################
# 1.5 ONE AWAY - There are three types of edits that can be performed on
# strings: insert a character, remove a character, or replace a character.
# Check if two strings are one or zero edits away.

def one_away(string1, string2):
    if string1 == string2:
        return True
    # Check for replace character
    elif len(string1) == len(string2):
        return one_edit_replace(string1, string2)
    # Check for insertion or removal
    elif len(string1) + 1 == len(string2):
        return one_edit_insert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return one_edit_insert(string2, string1)
    return False


# Check if there is only one character that has been replaced
def one_edit_replace(string1, string2):
    found_difference = False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if found_difference:
                return False
            else:
                found_difference = True
    return True


# Check if you can insert a character into string1 to make string2
def one_edit_insert(string1, string2):
    index1 = 0
    index2 = 0
    while (index2 < len(string2)) and (index1 < len(string1)):
        if string1[index1] != string2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

# Time Complexity: O(n) where n is the length of the shorter string

###############################################################################
# 1.6 STRING COMPRESSION - Implement a method to perform basic string
# compression using the counts of repeated characters. For example, the string
# aabcccccaaa will become a2b1c5a3. If the "compressed" string would not become
# smaller than the original string, your method should return the original
# string. Assume only uppercase and lowercase letters.


def string_compression(input_string):
    compressed_str = ""
    consecutive_count = 0

    for i in range(len(input_string)):
        consecutive_count += 1

    # If end of string or if next character is different from current, append
    # the character and count to the compressed string
        if ((i + 1) >= len(input_string)) or (input_string[i] !=
                                              input_string[i + 1]):
            compressed_str += "" + input_string[i] + str(consecutive_count)
            consecutive_count = 0

    if len(compressed_str) < len(input_string):
        return compressed_str
    else:
        return input_string

# Time Complexity: O(p + k**2) where p is the size of the original string and
# k is the number of consecutive character sequences

###############################################################################
# 1.7 ROTATE MATRIX - Given an image represented by an N x N matrix where each
# pixel is 4 bytes, write a method to rotate the image by 90 degrees.


def rotate_matrix(matrix):
    N = len(matrix)
    rotated_matrix = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_x = N - j - 1
            rotated_y = i
            rotated_matrix[rotated_x][rotated_y] = matrix[i][j]
    return rotated_matrix

# Time Complexity: O(n**2) since any algorithm must touch all N**2 elements

###############################################################################
# 1.8 ZERO MATRIX - If an element in an M x N matrix is 0, its entire row and
# column are set to 0


def zero_matrix(matrix):
    M = len(matrix)
    N = len(matrix[0])
    zero_rows = [False] * M
    zero_columns = [False] * N

    # Store the row and column index with value 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_columns[j] = True

    for i in range(M):
        if zero_rows[i]:
            nullifyRow(matrix, i)

    for j in range(N):
        if zero_columns[j]:
            nullifyColumn(matrix, j)

    return matrix


def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullifyColumn(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0

# Notes - To reduce space, you also use the first row as a replacement for the
# row array and the first column as a replacement for the column array. There
# would also need to be booleans to indicate whether the first row and column
# had zeros, and these would need to be nullifed in the end if necessary.

###############################################################################
# 1.9 STRING ROTATION - Given two strings, s1 and s2, write code to check if s2
# is a rotation of s1.


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    return s2 in s1s1

# Time Complexity: O(N) if we assume isSubstring runs in O(A+ B) time where
# A is the length of s1 and B is the length of s2

###############################################################################
# 2.1 REMOVE DUPS - Remove duplicates from unsorted linked list

# Notes - iterate through linked list, adding each element to dictionary
# When there is a duplicate element, remove the element and continue iterating.


class ListNode():

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def remove_dups(n: ListNode):
    elements = {}

    previous = ListNode()

    while n:
        # Duplicate exists
        if n.val in elements:
            previous.next = n.next
        else:
            elements[n.val] = 1
            previous = n
        n = n.next

# Time Complexity: O(N) where N is the number of elements in the linked list
# Notes - If there is no buffer, there can be two pointers:
# - current - iterates through linked list
# - runner - checks subsequent nodes for duplicates

###############################################################################
# 2.2 RETURN KTH TO LAST - Find the kth to last element of a singly linked list

# Recursive Solution: Create wrapper function


index = 0


def returnKthToLast(head: ListNode, k: int):
    return returnKthToLast(head, k, index)


def returnKthToLastWrapper(head: ListNode, k: int, index: int):
    if not head:
        return None

    node = returnKthToLastWrapper(head.next, k, index)
    index += 1
    if index == k:
        return head

    return node

# Space Complexity: O(n) - due to recursive calls

# Iterative Solution: Place two pointers (p1 and p2) k nodes apart and move
# them at the same pace. p2 will be at the beginning and p1 will be k nodes
# into the list


def returnKthToLastIterative(head: ListNode, k: int):
    p1 = head
    p2 = head

    # Move p1 k nodes into the list
    for i in range(k):
        if not p1:
            return None
        p1 = p1.next

    # Move pointers at same pace. When p1 hits the end, p2 will be at the
    # correct element
    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2

# Time Complexity: O(n)
# Space Complexity: O(1)

###############################################################################
# 2.3 DELETE MIDDLE NODE - delete a node in the middle of a singly linked list
# given only access to that node

# Notes - Copy the data from the next node over to the current node and then
# delete the next node


def deleteMiddleNode(mid: ListNode):
    mid.val = mid.next.val
    mid.next = mid.next.next



###############################################################################
###############################################################################

# TEST CODE BELOW
print(string_rotation("waterbottle", "wa"))
