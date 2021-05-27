'''
Generators
Next keyword givges the next yield statement
Yield keyword is used to get the next value in the statement
'''
import sys


def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(100)

print(next(values))
print(next(values))
print(next(values))

#Using itterations
for x in values:
    print(x)

#Using sys
print(sys.getsizeof(values))

#Creating infinite sequences - doesn't store any value, just yields the next value
def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))

