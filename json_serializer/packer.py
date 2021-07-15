from .json_constants import *
import builtins
import inspect
from types import FunctionType, CodeType


def get_type(name):
    try:
        return getattr(builtins, name)
    except:
        try:
            obj = globals()[name]
        except:
            raise AttributeError('Invalid type')
        return repr(obj) if isinstance(obj, type) else None


def is_iterable(obj):
    return hasattr(obj, '__iter__') and type(obj) != str


def pack(obj, root=False):
    if is_iterable(obj):
        return pack_iterable(obj, root)
    elif type(obj).__name__ in PRIMITIVES:
        return pack_primitive(obj, root)
    elif inspect.iscode(obj):
        return pack_code(obj)
    elif callable(obj):
        return pack_callable(obj)
    raise TypeError(f'Unknown type {type(obj)}')


def unpack(obj):
    if type(obj) == dict:
        if not '__type__' in obj.keys():
            raise Exception('No type key in dictionary')

        if obj['__type__'] in ITERABLES:
            return unpack_iterable(obj)
        elif obj['__type__'] in PRIMITIVES:
            return unpack_primitive(obj)
        elif obj['__type__'] == CODE_TYPE:
            return unpack_code(obj)
        elif obj['__type__'] == FUNCTION_TYPE:
            return unpack_callable(obj)
    elif type(obj).__name__ in ITERABLES:
        return unpack_iterable(obj)
    elif type(obj).__name__ in PRIMITIVES:
        return unpack_primitive(obj)
    raise Exception('Unknown type for unpacking')


def pack_iterable(obj, root):
    if type(obj) == dict:
        res = {'__type__': type(obj).__name__, 'value': []}
        for k, v in obj.items():
            res['value'].append([pack(k), pack(v)])
        return res
    else:
        res = []
        for item in obj:
            res.append(pack(item))
        if root or type(obj) != list:
            return {'__type__': type(obj).__name__, 'value': res}
        return res


def unpack_iterable(obj):
    if type(obj) == dict:
        if obj['__type__'] == dict.__name__:
            res = dict()
            for pair in obj['value']:
                res[unpack(pair[0])] = unpack(pair[1])
            return res
        elif obj['__type__'] in ITERABLES:
            obj_type = get_type(obj['__type__'])

            if obj_type == None:
                raise AttributeError('No type')

            res = []
            for item in obj['value']:
                res.append(unpack(item))

            return obj_type(res)
    else:
        res = []
        for item in obj:
            res.append(unpack(item))
        return res


def pack_primitive(obj, root):
    if type(obj) == complex:
        return {'__type__': type(obj).__name__, 'value': str(obj)}
    if root:
        return {'__type__': type(obj).__name__, 'value': obj}
    return obj


def unpack_primitive(obj):
    if type(obj).__name__ in PRIMITIVES:
        return obj
    elif type(obj) == dict and 'value' in obj.keys():
        if obj['__type__'] == complex.__name__:
            return complex(obj['value'])
        return obj['value']
    raise Exception('Cant unpack primitive')


def pack_code(obj):
    res = {'__type__': CODE_TYPE,
           'co_argcount': pack(obj.co_argcount),
           'co_posonlyargcount': pack(obj.co_posonlyargcount),
           'co_kwonlyargcount': pack(obj.co_kwonlyargcount),
           'co_nlocals': pack(obj.co_nlocals),
           'co_stacksize': pack(obj.co_stacksize),
           'co_flags': pack(obj.co_flags),
           'co_code': pack(obj.co_code),
           'co_consts': pack(obj.co_consts),
           'co_names': pack(obj.co_names),
           'co_varnames': pack(obj.co_varnames),
           'co_filename': pack(obj.co_filename),
           'co_name': pack(obj.co_name),
           'co_firstlineno': pack(obj.co_firstlineno),
           'co_lnotab': pack(obj.co_lnotab),
           'co_freevars': pack(obj.co_freevars),
           'co_cellvars': pack(obj.co_cellvars)
           }
    return res


def unpack_code(obj):
    res = CodeType(unpack(obj['co_argcount']),
                   unpack(obj['co_posonlyargcount']),
                   unpack(obj['co_kwonlyargcount']),
                   unpack(obj['co_nlocals']),
                   unpack(obj['co_stacksize']),
                   unpack(obj['co_flags']),
                   unpack(obj['co_code']),
                   unpack(obj['co_consts']),
                   unpack(obj['co_names']),
                   unpack(obj['co_varnames']),
                   unpack(obj['co_filename']),
                   unpack(obj['co_name']),
                   unpack(obj['co_firstlineno']),
                   unpack(obj['co_lnotab']),
                   unpack(obj['co_freevars']),
                   unpack(obj['co_cellvars']))
    return res


def get_globals_from_code(code, current_globals):
    res = {}
    for name in code.co_names:
        if name in current_globals and name != code.co_name:
            res[name] = current_globals[name]
        
    for item in code.co_consts:
        if inspect.iscode(item):
            res.update(get_globals_from_code(item, current_globals))
    return res


def pack_callable(obj):
    res = {'__type__': FUNCTION_TYPE,
           '__code__': pack(obj.__code__),
           '__globals__': pack(get_globals_from_code(obj.__code__, obj.__globals__))
           }
    return res


def unpack_callable(obj):
    func_globals = unpack(obj['__globals__'])
    func_globals['__builtins__'] = builtins
    
    new_func = FunctionType(unpack(obj['__code__']), func_globals)
    new_func.__globals__[new_func.__name__] = new_func
    return new_func
