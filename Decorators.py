'''
Decorators add a certain functionality to a function
'''

#Specific decorator
def mydecorator(function):
    def wrapper():
        function()
        print('I am decorating a function!')

    return wrapper

@mydecorator
def hello_world():
    print('Hello world!')

(hello_world)()


#Universal decorator
def mydecorator(function):
    def wrapper(*args, **kwargs):
        return_value =  function(*args, **kwargs)
        print('I am decorating a function!')
        return return_value

    return wrapper

@mydecorator
def hello(person):
    return f'Hello {person}!'

print(hello('Rhee'))

#Practical example - Logging
def logged(function):
    def wrapper(*args, **kwargs):
        value =  function(*args, **kwargs)
        with open('loglife.txt', 'a+') as f:
            fname = function.__name__
            print(f'{fname} returned value {value}')
            f.write(f'{fname} returned value {value}\n')
        return value

    return wrapper

@logged
def add (x, y):
    return x + y

print(add(10, 20))

#Practical example - Timing
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after-before} seconds to execute!')

def myfunction(x):
    result = 1
    for i in range(x):
        result *= 1
        return

