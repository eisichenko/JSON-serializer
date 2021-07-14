from json_serializer import *

d = complex(1, 2)

print(dumps(d))

print(loads(dumps(d)))

print(loads(dumps(d)) == d)
