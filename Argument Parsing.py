'''
It is mostly important for systems programming or getting into networking scripts
that are going to be executed on a command line.

myscript.py - 

def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])
    

myfunction('Hey', True, 25, '3rd year', KEYONE='TEST', KEYTWO=24)
'''

import sys

#Usage: main.py FILENAME

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)
