from .json_lexer import lex
from .json_parser import parse
from .json_constants import *


primitives = (int, bool, str, float, type(None))

def is_primitive(obj):
    return type(obj) in primitives


def loads(string):
    tokens = lex(string)
    result = parse(tokens)[0]
    return result


def dumps(obj):
    if type(obj) == dict:
        result = '{'
        
        for i, (key, val) in enumerate(obj.items()):
            result += f'{dumps(key)}: {dumps(val)}'

            if i < len(obj) - 1:
                result += ', '
            else:
                result += '}'

        return result
    elif type(obj) == list:
        result = '['
        list_len = len(obj)

        for i, val in enumerate(obj):
            result += dumps(val)

            if i < list_len - 1:
                result += ', '
            else:
                result += ']'

        return result
    elif type(obj) == str:
        return f'"{obj}"'
    elif type(obj) == bool:
        return 'true' if obj else 'false'
    elif type(obj) == type(None):
        return 'null'
    elif is_primitive(obj):
        return str(obj)
    raise Exception('Invalid object type')


def load(fp):
    fp.seek(0)
    string = fp.read()
    return loads(string)  


def dump(obj, fp):
    string = dumps(obj)
    fp.write(string)
    fp.flush()
