import random
import string


MAX_DEPTH = 6
MAX_LENGTH = 5
MAX_SET_LENGTH = 40


def random_int():
    return random.randint(-10_000,10_000)


def random_float():
    return float(random.random() * random.randint(1, 10_000))

                 
def random_complex():
    return complex(random_float(), random_float())


def random_string(n=random.randint(0, MAX_LENGTH)):
    symbols = string.digits + string.ascii_letters + ' '
    symbols = symbols.replace('\\', '')
    return ''.join(random.choice(symbols) for _ in range(n))


def random_bool():
    res = random.randint(0, 1)
    if res == 1:
        return True
    return False


def random_none():
    return None


def random_bytes():
    return bytes(random_string(), encoding='utf-8')


def random_bytearray(depth=0):
    return bytearray(random_string(), encoding='utf-8')


def random_tuple(n=random.randint(0,MAX_LENGTH), depth=0, is_hashable=False):
    if depth >= MAX_DEPTH:
        return tuple()
    
    res = []
    for _ in range(n):
        if is_hashable:
            func = random.choice(hashable)
        else:
            func = random.choice(all_values)
        
        if func == random_tuple:
            value = func(depth=depth+1, is_hashable=is_hashable)
        elif func in random_iterables:
            value = func(depth=depth+1)
        else:
            value = func()
            
        res.append(value)
    return tuple(res)


def random_set(n=random.randint(0, MAX_SET_LENGTH), depth=0):
    if depth >= MAX_DEPTH:
        return set()
    
    res = set()
    for _ in range(n):
        func = random.choice(hashable)
        
        if func == random_tuple:
            value = func(depth=depth+1, is_hashable=True)
        else:
            value = func()
            
        res.add(value)
    return res


def random_frozenset(n=random.randint(0, MAX_SET_LENGTH), depth=0):
    if depth >= MAX_DEPTH:
        return frozenset()
    
    return frozenset(random_set(n=n, depth=depth+1))


def random_list(n=random.randint(0, MAX_LENGTH), depth=0):
    if depth >= MAX_DEPTH:
        return []
    
    res = []
    for _ in range(n):
        func = random.choice(all_values)
        
        if func in random_iterables:
            value = func(depth=depth+1)
        else:
            value = func()
            
        res.append(value)
    return res


def random_dict(n=random.randint(0, MAX_LENGTH), depth=0):
    if depth >= MAX_DEPTH:
        return {}
    
    res = {}
    
    for _ in range(n):
        key_func = random.choice(hashable)
        if key_func == random_tuple:
            key = key_func(depth=depth+1, is_hashable=True)
        else:
            key = key_func()
        
        while key in res.keys():
            key_func = random.choice(hashable)
            if key_func == random_tuple:
                key = key_func(depth=depth+1, is_hashable=True)
            else:
                key = key_func()
            
        func = random.choice(all_values)
        
        if func in random_iterables:
            value = func(depth=depth+1)
        else:
            value = func()
            
        res[key] = value
    return res


def random_iterable():
    return random.choice([random_dict, random_list, random_set, random_tuple])()


random_primitives = [random_int, 
                     random_float, 
                     random_complex, 
                     random_string, 
                     random_bool, 
                     random_none, 
                     random_bytes
                     ]

random_iterables = [random_dict, random_list, random_bytearray, random_set, random_tuple]

hashable = random_primitives + [random_tuple]
all_values = random_iterables + random_primitives
