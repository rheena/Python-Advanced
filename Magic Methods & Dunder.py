'''
Dunder - Double underscores 
Used in constructors, deconstructors
'''

#Constructors
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Magic method
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):         #Gives proper representaion of the vector
        return f'X: {self.x}, Y: {self.y}'

    def __len__(self):      #Defines the length of the object
        return 10

    def __call__(self):
        print('Hello! You called me?')

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2


print(v3)
print(len(v3))
v3()

'''
#Deconstructor
    def __del__(self):
        print('Object is being deconstructed!')
'''

