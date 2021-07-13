from json_serializer import *

# d = { 1: 'a', 'asd': { True: 123, None: [ {1:'a'}, 2, False] }}

d = {'a': {'b': {1: 2}}}

s = dumps(d)

print(s)

new = loads(s)

print(new)
print(new == d)