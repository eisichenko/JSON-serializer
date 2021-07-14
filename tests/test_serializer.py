from json_serializer.json_parser import parse_dict
import pytest
from .simple_objects import *
from json_serializer import *
import os


@pytest.fixture()
def file_fixture():
    with open('tests/temp_file_for_tests.txt', 'w+') as fp:
        yield fp
    os.remove('tests/temp_file_for_tests.txt')


@pytest.mark.parametrize('obj', sample_dicts)
def test_dictionaries(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', sample_lists)
def test_lists(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', sample_sets)
def test_sets(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', test_recursion)
def test_simple_recursion(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj
    

@pytest.mark.parametrize('obj', single_primitives)
def test_single_primitives(obj):
    json = dumps(obj)
    assert json[0] == '{'
    new_obj = loads(json)
    assert new_obj == obj


@pytest.mark.parametrize('obj', sample_bins)
def test_bin_types(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj

    
@pytest.mark.parametrize('obj', sample_dicts)
def test_files(file_fixture, obj):
    dump(obj, file_fixture)
    new_obj = load(file_fixture)
    assert new_obj == obj


def test_exceptions():
    with pytest.raises(Exception):
        loads('[1 2 3]')
    with pytest.raises(Exception):
        loads('{1:2 3:4}')
    with pytest.raises(Exception):
        loads('[1, 2, 3')
    with pytest.raises(Exception):
        loads('{"1": 2, "3": 4')
    with pytest.raises(Exception):
        loads('{')
    with pytest.raises(Exception):
        loads('{"1": 2, "3" 4}')
    with pytest.raises(Exception):
        loads('{"1": 2, 3: 4}')
    with pytest.raises(Exception):
        loads('{"1": 2 "3": 4}')
    with pytest.raises(Exception):
        parse_dict(['}'])
    with pytest.raises(SyntaxError):
        loads('"a')
    with pytest.raises(SyntaxError):
        loads('{1: 2 @}')
    with pytest.raises(Exception):
        dumps(os)
    with pytest.raises(Exception):
        parse(['LOL'], is_root=True)
    with pytest.raises(Exception):
        unpack({})
    with pytest.raises(Exception):
        unpack(os)
