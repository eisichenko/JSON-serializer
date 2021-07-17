from .functions import *

CONST = 123

class A():
    class B():
        @classmethod
        def fib(cls, n):
            if n < 3:
                return 1
            return cls.fib(n - 1) + cls.fib(n - 2)
        
        def hello():
            return 'HELLO FROM B'

    CLASS_VAR = 666
    l = lambda x: x ** 99
    f = say_hi
    
    def __init__(self, name):
        self.name = name
        a = CONST

    def get_name(self):
        return self.name
    
    def get_fib(self, n):
        return self.B.fib(n)
    
    def __str__(self):
        return self.name + self.B.hello()
    

class B:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def get_str_age(self):
        return 'Your age is ' + str(self.get_age())

    @staticmethod
    def say_hello():
        return 'hello'

    class_var = 123
    
    
class C():
    def f(self):
        return 'HI FROM C'

class D():
    def f(self):
        return 'HI FROM D'

class E(C, D):
    def g(self):
        return 'ANOTHER FUNC' 

class G(E):
    pass


class H():
    CLASS_VAR = CONST