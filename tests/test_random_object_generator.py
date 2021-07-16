from .simple_object_generator import *
import pytest

def test_generators():
    assert type(random_int()) == int
    assert type(random_float()) == float
    assert type(random_complex()) == complex
    assert type(random_string()) == str
    assert type(random_bool()) == bool
    assert type(random_none()) == type(None)
    assert type(random_bytes()) == bytes
    assert type(random_bytearray()) == bytearray
    assert type(random_tuple(n=10)) == tuple
    assert type(random_set(n=10)) == set
    assert type(random_frozenset(n=10)) == frozenset
    assert type(random_list(n=10)) == list
    assert type(random_dict(n=10)) == dict
    assert hasattr(random_iterable(), '__iter__')
    
    t = random_tuple(n=10, is_hashable=True)
    s = set()
    s.add(t)
    
    assert len(s) == 1
    
    t = random_tuple(n=10, is_hashable=False)
    s = set()
    with pytest.raises(TypeError):
        s.add(t)
        

def test_max_depth():
    assert len(random_tuple(n=10, depth=1e9)) == 0
    assert len(random_set(n=10, depth=1e9)) == 0
    assert len(random_frozenset(n=10, depth=1e9)) == 0
    assert len(random_list(n=10, depth=1e9)) == 0
    assert len(random_dict(n=10, depth=1e9)) == 0
    

def test_dict_tuple_key():
    from . import simple_object_generator
    tmp = simple_object_generator.hashable
    simple_object_generator.hashable = [random_tuple]
    d = random_dict(n=1, depth=MAX_DEPTH-1)
    assert type(d) == dict
    for k in d:
        assert type(k) == tuple
    simple_object_generator.hashable = tmp
