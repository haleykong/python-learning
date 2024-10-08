# LIST COMPREHENSION
# - Create lists based on other lists instead of using for loops

# Double prize money weekend bonanza
prizes = [5, 10, 50, 100, 1000]

# for loop method
dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize * 2)
print(dbl_prizes)


# comprehension method
# 1) What you want to add to the list
# 2) What you're cycling through
# 3) Any conditions
dbl_prizes = [prize * 2 for prize in prizes]
print(dbl_prizes)

# Squaring numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for loop method
squared_even_nums = []
for num in nums:
    if (num ** 2) % 2 == 0:
        squared_even_nums.append(num ** 2)
print(squared_even_nums)

# comprehension method
squared_even_numbs = [num ** 2 for num in nums if (num ** 2) % 2 == 0]
print(squared_even_nums)
