from json_serializer import *
import inspect
from tests.samples.functions import *
from tests.samples.class_types import *
from pprint import pprint


def smth(f):
    def wrapper(*args, **kwargs):
        res = f()
        print('HI')
        return res
    return wrapper

# @smth
# def f():
#     return 'HELLO'

# def f1():
#     return 'HELLO'

class A():
    def __init__(self, name):
        self.name = name
        
    def f(self):
        return 'YAY!'

class Simple():
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
a = Simple('qweqwe')

print(loads(dumps(a)))
