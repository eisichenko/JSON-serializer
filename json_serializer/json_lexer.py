from .json_constants import *


def lex_string(string, cur_index):
    if string[cur_index] == JSON_QUOTE:
        cur_index += 1
    else:
        return None, cur_index
    
    result = ''
    
    i = cur_index
    
    while i < len(string):
        if i < len(string) - 1 and string[i] == '\\' and string[i + 1] == '"':
            result += string[i + 1]
            i += 1
        elif string[i] == JSON_QUOTE:
            return result, i + 1
        else:
            result += string[i]
        i += 1
        
    raise SyntaxError('Expected end of string quote')


def lex_number(string, cur_index):
    result = ''
    
    i = cur_index

    while i < len(string) and string[i] in NUMBER_CHARACTERS:
        result += string[i]
        i += 1
    
    try:
        if '.' in result:
            return float(result), i

        return int(result), i
    except:
        return None, cur_index


def lex_bool(string, cur_index):
    if len(string) - cur_index + 1 >= len(JSON_TRUE):
        i = cur_index
        j = 0
        
        while j < len(JSON_TRUE) and string[i] == JSON_TRUE[j]:
            i += 1
            j += 1
        
        if j == len(JSON_TRUE):
            return True, i
        
    if len(string) - cur_index + 1 >= len(JSON_FALSE):
        i = cur_index
        j = 0
        
        while j < len(JSON_FALSE) and string[i] == JSON_FALSE[j]:
            i += 1
            j += 1
        
        if j == len(JSON_FALSE):
            return False, i

    return None, cur_index


def lex_null(string, cur_index):
    if len(string) - cur_index + 1 >= len(JSON_NULL):
        i = cur_index
        j = 0
        
        while j < len(JSON_NULL) and string[i] == JSON_NULL[j]:
            i += 1
            j += 1
        
        if j == len(JSON_NULL):
            return True, i

    return None, cur_index


def lex(string):
    tokens = []
    
    i = 0

    while i < len(string):
        result, i = lex_string(string, i)
        if result is not None:
            tokens.append(result)
            continue

        result, i = lex_number(string, i)
        if result is not None:
            tokens.append(result)
            continue

        result, i = lex_bool(string, i)
        if result is not None:
            tokens.append(result)
            continue

        result, i = lex_null(string, i)
        if result is not None:
            tokens.append(None)
            continue

        if string[i] in JSON_WHITESPACE:
            i += 1
            continue
        elif string[i] in JSON_SYNTAX:
            tokens.append(string[i])
            i += 1
            continue
        else:
            raise SyntaxError(f'Unexpected character: {string[i]}')

    return tokens
