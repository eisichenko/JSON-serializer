from json_serializer import *



d = bytes([1, 2, 3, 2])

d = bytearray('LOLOLOLOLOLOLO', encoding='utf-8')


print(dumps(d))

print(loads(dumps(d)))

print(loads(dumps(d)) == d)
