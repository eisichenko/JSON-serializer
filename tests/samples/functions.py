CONST = 123
QWE = 666

def say_hi():
    return 'hello from say_hi'


def f():
    def g():
        def h():
            return say_hi()
        return str(CONST) + h()
    return g() + str(QWE) + say_hi()


def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def function_with_args(a, b = 'default', *args):
    local_var = a * 3
    qwe = CONST
    return str(local_var) + b + str(len(args))


simple_lambda = lambda x : x ** 2


nested_lambda_with_global = lambda x : lambda y : str((x + y) / 2 ** CONST + fib(5)) + say_hi()


def local_and_global_func_and_lambda(n):
    def h(n):
        return n ** 2

    l = lambda n: n ** 0.5

    return str(l(h(n) + h(n))) + nested_lambda_with_global(1)(2)


def func_with_nested_class(string):
    class B():
        def f(self):
            return CONST
    return str(B().f()) + string


def smth_decorator(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return str(res) + "HI!!!"
    return wrapper

def smth_decorator1(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return str(res) + "HELL!!!"
    return wrapper


@smth_decorator
@smth_decorator1
def func_with_decorators(string):
    return string


def function_with_defaults(a, b=123, c='asd', *args, **kwargs):
    return str(a) + str(b) + str(c) + str(args) + str(kwargs)
