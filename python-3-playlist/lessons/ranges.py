# RANGE: generates list of numbers that can then be iterated over with a for
# loop

# Generates list of numbers from 0 to number (not inclusive)
for n in range(5):
    print(n)

# Generates list of numbers from start number (inclusive) to
# end number (not inclusive)
for n in range(3, 10):
    print(n)

# Generates list of numbers from start number (inclusive) to
# end number (not inclusive) with given step size
for n in range(0, 20, 4):
    print(n)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

for n in range(len(burgers)):
    print(n, burgers[n])

for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])
