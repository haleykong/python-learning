# FILTERS
# - Filter out values from collection based on a function's result

grades = ['A', 'B', 'F', 'C', 'F', 'A']


def remove_fails(grade):
    return grade != 'F'

# Filter function returns True or False. If it returns True, then it stays in
# the list
# print(list(filter(remove_fails, grades)))

# for loop
# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
# print(filtered_grades)

# comprehension method
print([grade for grade in grades if grade != 'F'])
