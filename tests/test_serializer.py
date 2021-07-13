import pytest
from .simple_objects import *
from json_serializer import *
import os


@pytest.mark.parametrize('obj', sample_dicts)
def test_dictionaries(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj


@pytest.mark.parametrize('obj', sample_lists)
def test_lists(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj

    
@pytest.fixture()
def file_fixture():
    with open('tests/temp_file_for_tests.txt', 'w+') as fp:
        yield fp
    os.remove('tests/temp_file_for_tests.txt')

    
@pytest.mark.parametrize('obj', sample_dicts)
def test_files(file_fixture, obj):
    dump(obj, file_fixture)
    new_obj = load(file_fixture)
    assert new_obj == obj