class Simple():
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return (self.name == other.name and
                self.get_name() == other.get_name() and
                self.__class__.__name__ == other.__class__.__name__ and
                str(self) == str(other))

    
class Medium:
    a = 666
    b = [333, 666, 'www']

    
    @staticmethod
    def c(n):
        return str(n) + '!!!'
    
    
    @staticmethod
    def d():
        return 'Hello from B class method'


    def __eq__(self, other):
        obj1 = type(self)
        obj2 = type(self)
        
        return (obj1.a == obj2.a and
                obj1.b == obj2.b and
                obj1.c(123) == obj2.c(123) and
                obj1.d() == obj2.d() and
                self.__class__.__name__ == other.__class__.__name__)


def recursive_fib(n):
    if n < 2:
        return 1

    return recursive_fib(n - 1) + recursive_fib(n - 2)


def func_with_positional_args(a, b = 'default', *args):
    local_var = a * 3
    return str(local_var) + str(b) + str(len(args))


class Hard:
    def __init__(self, name):
        self.none = None
        self.name = name
        self.arr = [1, "some string", func_with_positional_args, Medium]
        self.a = 1
        self.b = -123.123
        self.c = "abacaba"
        self.d = True
        self.e = False

        self.set = {123, 'qwe', 'rty', False, True, None, (-123.1, False)}
        self.tuple = ('qwe', 'rty', 6666666, {1, 2, 3, False, ('haha', 'nooo', 7777, -131.31313), True, None})
        self.dict = {1: 1, 2: 4, 3: 9, 4: recursive_fib, 5: Medium, 6: {5 : {7: [1, 2, 3]}}}

        self.l = lambda x: x ** 2
        self.func = func_with_positional_args
        
        self.g = Simple('TTT')

    
    def get_name(self):
        return self.name

    
    def set_name(self, string):
        self.name = string
        
    
    def __eq__(self, other):
        return (self.none == other.none and
                self.name == other.name and
                
                self.arr[0] == other.arr[0] and
                self.arr[1] == other.arr[1] and
                self.arr[2](1, 2, 3, 4, 5) == other.arr[2](1, 2, 3, 4, 5) and
                self.arr[3]() == other.arr[3]() and
                
                self.a == other.a and
                self.b == other.b and
                self.c == other.c and
                self.d == other.d and
                self.e == other.e and
                self.set == other.set and
                self.tuple == other.tuple and
                
                self.dict[1] == other.dict[1] and
                self.dict[2] == other.dict[2] and
                self.dict[3] == other.dict[3] and
                self.dict[4](7) == other.dict[4](7) and
                self.dict[5]() == other.dict[5]() and
                self.dict[6] == other.dict[6] and
                
                self.l(123) == other.l(123) and
                self.func(a=123, b=6) == other.func(a=123, b=6) and
                self.g == other.g and
                self.get_name() == other.get_name() and
                self.set_name('qweqweqwe') == other.set_name('qweqweqwe') and
                self.get_name() == other.get_name() and
                self.set_name('RRR') == other.set_name('RRR') and
                self.get_name() == other.get_name() and
                
                self.__class__.__name__ == other.__class__.__name__)


class Vector():
    def __init__(self, arr):
        self._arr = arr
        self._index = 0
        
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index >= len(self._arr):
            raise StopIteration()
        
        res = self._arr[self._index]
        self._index += 1
        
        return res
