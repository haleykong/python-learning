# FUNCTIONS
# Create block of code that can be called elsewhere in code

# Can set default parameters
def greet(name='ryu', time='morning'):
    print(f'Good {time} {name}, hope you are well')


# name = input('enter your name: ')
# time = input('enter the time of day: ')

# greet(name, time)

def area(radius):
    return 3.142 * radius * radius


def vol(area, length):
    print(area * length)


radius = int(input('enter a radius: '))
length = int(input('enter a length: '))

vol(area(radius), length)
