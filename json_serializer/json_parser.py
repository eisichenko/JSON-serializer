from .json_constants import *


def parse_list(tokens, index):
    json_array = []

    t = tokens[index]
    if t == JSON_RIGHTBRACKET:
        return json_array, index + 1

    while index < len(tokens):
        json, index = parse(tokens, index)
        json_array.append(json)
        
        if index >= len(tokens):
            break

        t = tokens[index]
        if t == JSON_RIGHTBRACKET:
            return json_array, index + 1
        elif t != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            index += 1
    raise Exception('Expected end-of-array bracket')


def parse_dict(tokens, index):
    json_object = {}

    if index >= len(tokens):
        raise Exception('Expected end-of-object brace')

    if tokens[index] == JSON_RIGHTBRACE:
        raise Exception('Empty dictionary is invalid')

    while index < len(tokens):
        key = tokens[index]
        if type(key) == str:
            index += 1
        else:
            raise Exception(f'Expected string key, got: {key}')
        
        if tokens[index] != JSON_COLON:
            raise Exception(f'Expected colon after key in object, got: {tokens[index]}')

        value, index = parse(tokens, index + 1)
        
        if index >= len(tokens):
            break

        json_object[key] = value

        t = tokens[index]
        if t == JSON_RIGHTBRACE:
            return json_object, index + 1
        elif t != JSON_COMMA:
            raise Exception(f'Expected comma after pair in object, got: {t}')

        index += 1

    raise Exception('Expected end-of-object brace')

def parse(tokens, index=0):
    
    index = index
    
    t = tokens[index]

    if index == 0 and t != JSON_LEFTBRACE:
        raise Exception('Root must be an object')

    if t == JSON_LEFTBRACKET:
        return parse_list(tokens, index + 1)
    elif t == JSON_LEFTBRACE:
        return parse_dict(tokens, index + 1)
    else:
        return t, index + 1
