num1 = 3.1425467389
num2 = 10.2903948

# PREVIOUS WAY
print('num 1 is', num1, 'and num 2 is', num2)

# FORMAT METHOD
# Pass in formatting of precision (number of digits)
print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))

# Pass in formatting of decimals (numbers after decimal point)
print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2))

# F-STRING METHOD
print(f'num 1 is {num1:.4f} and num 2 is {num2:.4f}')