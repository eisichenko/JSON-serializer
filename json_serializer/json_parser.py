from .json_constants import *


def parse_list(tokens):
    json_array = []

    t = tokens[0]
    if t == JSON_RIGHTBRACKET:
        return json_array, tokens[1:]

    while len(tokens) > 0:
        json, tokens = parse(tokens)
        json_array.append(json)
        
        if len(tokens) == 0:
            break

        t = tokens[0]
        if t == JSON_RIGHTBRACKET:
            return json_array, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]
    raise Exception('Expected end-of-array bracket')


def parse_dict(tokens):
    json_object = {}

    if len(tokens) == 0:
        raise Exception('Expected end-of-object brace')

    if tokens[0] == JSON_RIGHTBRACE:
        return json_object, tokens[1:]

    while len(tokens) > 0:
        json_key = tokens[0]
        
        tokens = tokens[1:]
        
        if tokens[0] != JSON_COLON:
            raise Exception(f'Expected colon after key in object, got: {t}')

        json_value, tokens = parse(tokens[1:])
        
        if len(tokens) == 0:
            break

        json_object[json_key] = json_value

        t = tokens[0]
        if t == JSON_RIGHTBRACE:
            return json_object, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception(f'Expected comma after pair in object, got: {t}')

        tokens = tokens[1:]

    raise Exception('Expected end-of-object brace')

def parse(tokens):
    t = tokens[0]

    if t == JSON_LEFTBRACKET:
        return parse_list(tokens[1:])
    elif t == JSON_LEFTBRACE:
        return parse_dict(tokens[1:])
    else:
        return t, tokens[1:]