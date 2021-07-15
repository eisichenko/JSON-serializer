from .functions import *
from json_serializer import *


def test_functions_with_globals():
    assert loads(dumps(f))() == f()
    assert loads(dumps(function_with_args(1, 'asd', 1, 2, 3))) == function_with_args(1, 'asd', 1, 2, 3)
    assert loads(dumps(local_and_global_func_and_lambda(123))) == local_and_global_func_and_lambda(123)
    

def test_multiple_pack_and_unpack():
    assert unpack(pack(unpack(pack(unpack(pack(fib))))))(7) == fib(7)


def test_lambdas():
    assert simple_lambda(123) == loads(dumps(simple_lambda))(123)
    assert nested_lambda_with_global(666)(1313) == loads(dumps(nested_lambda_with_global(666)(1313)))
