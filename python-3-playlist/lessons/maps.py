# MAPS
# - Take a list, apply a function to each item in list, return new list with
# updated items in it
from random import shuffle


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# map(function, data)
# print(list(map(jumble, words)))

print([jumble(word) for word in words])
