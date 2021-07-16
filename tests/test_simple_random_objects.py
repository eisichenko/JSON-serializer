import pytest
from .simple_object_generator import *
from json_serializer import *

NUMBER_OF_TESTS = 30

@pytest.mark.parametrize('obj', [random_dict() for _ in range(NUMBER_OF_TESTS)])
def test_dictionaries(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj
    

@pytest.mark.parametrize('obj', [random_list() for _ in range(NUMBER_OF_TESTS)])
def test_lists(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', [random_set() for _ in range(NUMBER_OF_TESTS)])
def test_sets(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', [random_frozenset() for _ in range(NUMBER_OF_TESTS)])
def test_frozensets(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', [random_tuple() for _ in range(NUMBER_OF_TESTS)])
def test_tuples(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', [random_iterable() for _ in range(NUMBER_OF_TESTS)])
def test_mixed(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj

