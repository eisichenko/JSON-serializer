from json_serializer import *
import inspect
from tests.functions import *
from pprint import pprint


class A():
    def f(self):
        return 'OBJ'

# pprint(dict(inspect.getmembers(fib.__code__)))

test = local_and_global_func_and_lambda

pprint(pack(test))

new_f = unpack(pack(unpack(pack(test))))

print(new_f.__name__)

print(new_f)
print(new_f(123))

print(test(123))

