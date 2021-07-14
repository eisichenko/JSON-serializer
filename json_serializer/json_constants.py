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

FALSE_LEN = len('false')
TRUE_LEN = len('true')
NULL_LEN = len('null')


ITERABLES = {dict.__name__,
             list.__name__,
             tuple.__name__,
             set.__name__,
             frozenset.__name__,
             bytes.__name__,
             bytearray.__name__,
             memoryview.__name__
             }

PRIMITIVES = {int.__name__,
              complex.__name__,
              str.__name__,
              float.__name__,
              bool.__name__,
              type(None).__name__
              }

ALL_TYPES = ITERABLES.union(PRIMITIVES)
