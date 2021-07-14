from .json_lexer import lex
from .json_parser import parse
from .json_constants import *
from .packer import *


def loads(string):
    tokens = lex(string)
    result = parse(tokens)[0]
    return unpack(result)


def dumps(obj):
    return json_dumps(pack(obj, root=True))


def json_dumps(obj):
    if type(obj) == dict:
        if len(obj.items()) == 0:
            raise Exception('Empty dictionary is invalid')
        
        result = '{'
        
        for i, (key, val) in enumerate(obj.items()):
            if type(key) != str:
                raise TypeError(f'Expected string key, but got {key}')
            
            result += f'"{key}": {json_dumps(val)}'

            if i < len(obj) - 1:
                result += ', '
            else:
                result += '}'

        return result
    elif type(obj) == list:
        if len(obj) == 0:
            return '[]'
        
        result = '['

        for i, val in enumerate(obj):
            result += json_dumps(val)

            if i < len(obj) - 1:
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
    elif type(obj).__name__ in PRIMITIVES:
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
