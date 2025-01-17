# timethis.py
# to compute how long it takes a function to execute

# Exercise 7.10

import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
        return r
    return wrapper
