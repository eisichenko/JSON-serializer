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
