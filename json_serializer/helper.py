import inspect


def bind_methods(instance):
    methods = dict(inspect.getmembers(instance, inspect.isfunction))

    for method in methods:
        cur_method = methods[method]

        args = list(inspect.signature(cur_method).parameters)
        
        if len(args) > 0 and args[0] == 'cls' and inspect.isclass(instance):
            bind_method(instance, cur_method)
        elif len(args) > 0 and args[0] == 'self' and not inspect.isclass(instance):
            bind_method(instance, cur_method)


def bind_method(instance, func, as_name=None):

    if as_name == None:
        as_name = func.__name__
    
    bound_method = func.__get__(instance, instance.__class__)
    
    setattr(instance, as_name, bound_method)
    

def make_cell(val=None):
    if val == None:
        return None
    x = val
    def closure():
        return x
    return closure.__closure__[0]
