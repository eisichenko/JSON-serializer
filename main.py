# you can test loads and dumps here yourself

from json_serializer import *

def f():
    return 'HI'

new = loads(dumps(f))

print(new())
