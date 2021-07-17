from .samples.functions import *
from .samples.class_types import *
from .samples.object_types import *
from json_serializer import *
import pytest


def test_get_type_from_string():
    assert list == get_type('list')
    
    with pytest.raises(AttributeError):
        get_type('AJSKDJASDJAKSFH')


def test_functions_with_globals():
    assert loads(dumps(f))() == f()
    assert loads(dumps(function_with_args(1, 'asd', 1, 2, 3))) == function_with_args(1, 'asd', 1, 2, 3)
    assert loads(dumps(local_and_global_func_and_lambda(123))) == local_and_global_func_and_lambda(123)
    assert loads(dumps(func_with_nested_class))('HAHAHAH') == func_with_nested_class('HAHAHAH')
    

def test_multiple_pack_and_unpack():
    assert unpack(pack(unpack(pack(unpack(pack(fib))))))(7) == fib(7)


def test_lambdas():
    assert simple_lambda(123) == loads(dumps(simple_lambda))(123)
    assert nested_lambda_with_global(666)(1313) == loads(dumps(nested_lambda_with_global(666)(1313)))


def test_functions_with_decorators():
    assert func_with_decorators('SOME MESSAGE') == loads(dumps(func_with_decorators))('SOME MESSAGE')


def test_functions_with_defaults():
    assert function_with_defaults(999) == loads(dumps(function_with_defaults))(999)
    assert function_with_defaults(a=13) == loads(dumps(function_with_defaults))(a=13)
    assert function_with_defaults(55, 64) == loads(dumps(function_with_defaults))(55, 64)
    assert function_with_defaults(999, 12333, -123) == loads(dumps(function_with_defaults))(999, 12333, -123)
    assert function_with_defaults(a=999, b=12333, c=-123) == loads(dumps(function_with_defaults))(a=999, b=12333, c=-123)
    
    with pytest.raises(TypeError):
        assert function_with_defaults() == loads(dumps(function_with_defaults))()

    assert function_with_defaults(999, 0, 'qwe', 3, 1, 2, 6, PRESS=666, F=131313) == loads(dumps(function_with_defaults))(999, 0, 'qwe', 3, 1, 2, 6, PRESS=666, F=131313)


def test_class_A():
    new_type = loads(dumps(A))
    new_obj = new_type('LOL')
    obj = A('LOL')
    
    assert obj.get_name() == new_obj.get_name()
    assert str(obj) == str(new_obj)
    assert type(obj).__name__ == type(new_obj).__name__
    assert obj.get_fib(7) == new_obj.get_fib(7)
    assert new_type.l(5) == A.l(5)
    assert new_type.f() == A.f()
    

def test_class_B():
    b = loads(dumps(B))
    
    new_obj = b(666)
    obj = B(666)
    

    assert new_obj.get_age() == obj.get_age()
    assert new_obj.class_var == obj.class_var
    assert new_obj.get_str_age() == obj.get_str_age()
    assert b.say_hello() == B.say_hello()
    

def test_inheritance():
    new = loads(dumps(G))
    assert tuple(map(lambda x: x.__name__, new.__bases__)) == tuple(map(lambda x: x.__name__, G.__bases__))
    assert new().f() == G().f()
    assert new().g() == G().g()
    
    new = loads(dumps(E))
    assert tuple(map(lambda x: x.__name__, new.__bases__)) == tuple(map(lambda x: x.__name__, E.__bases__))
    assert new().f() == E().f()
    assert new().g() == E().g()


def test_class_H():
    new = loads(dumps(H))
    assert new.CLASS_VAR == H.CLASS_VAR
    

def test_class_Vector():
    arr = [i for i in range(100)]
    obj = Vector(arr)
    new = loads(dumps(Vector))(arr)
    
    res_obj = []
    res_new = []
    
    for i in new:
        res_new.append(i)
    
    for i in obj:
        res_obj.append(i)
    
    assert res_obj == res_new

    

def test_objects():
    obj = Simple('qweqwe')
    new = loads(dumps(obj))
    assert obj == new

    obj = Medium()
    new = loads(dumps(obj))
    assert obj == new
    
    obj = Hard('AHAHAH')
    new = loads(dumps(obj))
    assert obj == new
    
    obj = [Simple('GGG'), Medium(), Hard('JJJ')]
    new = loads(dumps(obj))
    assert obj[0] == new[0]
    assert obj[1] == new[1]
    assert obj[2] == new[2]


def test_inheritance_in_objects():
    obj = G()
    new = loads(dumps(obj))
    
    assert obj.f() == new.f()
    assert obj.g() == new.g()
    

def test_iterable_objects():
    arr = [i for i in range(100)]
    obj = Vector(arr)
    new = loads(dumps(obj))
    
    res_obj = []
    res_new = []
    
    for i in new:
        res_new.append(i)
    
    for i in obj:
        res_obj.append(i)
    
    assert res_obj == res_new
