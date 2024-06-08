# CLASSES
# - Blueprint for how an object looks and behaves (e.g. properties)

class Planet:

    # Class-level attribute, which is the same for all instances
    shape = 'round'

    # init function runs every time we create an instance of this class
    # Self refers to the instance of the object being created
    # Create instance properties
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # Create instance methods
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    # Class-level method
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    # Static method
    # Only has access to parameters that were passed
    # Can be used on instance and class
    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}'


# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'the gravity is: {hoth.gravity}')
# print(hoth.orbit())

# print(f'Name: {naboo.name}')
# print(f'Radius: {naboo.radius}')
# print(f'Gravity: {naboo.gravity}')
# print(naboo.orbit())
