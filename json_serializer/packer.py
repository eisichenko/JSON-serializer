from .json_constants import *
import builtins

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
    raise TypeError(f'Unknown type {type(obj)}')


def unpack(obj):
    if type(obj) == dict:
        if not '__type__' in obj.keys():
            raise Exception('No type key in dictionary')
        
        if obj['__type__'] in ITERABLES:
            return unpack_iterable(obj)
        elif obj['__type__'] in PRIMITIVES:
            return unpack_primitive(obj)
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
    res = obj
    if root:
        return {'__type__': type(obj).__name__, 'value': res}
    return res


def unpack_primitive(obj):
    if type(obj).__name__ in PRIMITIVES:
        return obj
    elif type(obj) == dict and 'value' in obj.keys():
        return obj['value']
    raise Exception('Cant unpack primitive')
