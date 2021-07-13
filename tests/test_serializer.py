import pytest
from .simple_objects import *
from json_serializer import *

@pytest.mark.parametrize('obj', sample_dicts)
def test_dictionaries(obj):
    new_obj = loads(dumps(obj))
    assert new_obj == obj