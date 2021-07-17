JSON_COMMA = ','
JSON_COLON = ':'
JSON_LEFTBRACKET = '['
JSON_RIGHTBRACKET = ']'
JSON_LEFTBRACE = '{'
JSON_RIGHTBRACE = '}'
JSON_QUOTE = '"'

JSON_WHITESPACE = [' ', '\t', '\b', '\n', '\r']
JSON_SYNTAX = [JSON_COMMA, JSON_COLON, JSON_LEFTBRACKET, JSON_RIGHTBRACKET,
               JSON_LEFTBRACE, JSON_RIGHTBRACE]

JSON_FALSE = 'false'
JSON_TRUE = 'true'
JSON_NULL = 'null'


NUMBER_CHARACTERS = [str(digit) for digit in range(0, 10)] + ['-', 'e', '.']


ITERABLES = {dict.__name__,
             list.__name__,
             tuple.__name__,
             set.__name__,
             frozenset.__name__,
             bytes.__name__,
             bytearray.__name__
             }

PRIMITIVES = {int.__name__,
              complex.__name__,
              str.__name__,
              float.__name__,
              bool.__name__,
              type(None).__name__
              }

CODE_TYPE = 'code'
FUNCTION_TYPE = 'function'
CLASS_TYPE = 'class'
OBJECT_TYPE = 'object'

COMPLEX = {FUNCTION_TYPE, CLASS_TYPE, OBJECT_TYPE, CODE_TYPE}

ALL_TYPES = ITERABLES.union(PRIMITIVES).union(COMPLEX)
