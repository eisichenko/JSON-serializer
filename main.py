from json_serializer import *
from tests.samples.functions import *
from tests.samples.class_types import *
from tests.samples.object_types import *
from pprint import pprint





pprint(unpack(pack(f))())

# print(f.__closure__[0].cell_contents)

# a = f.__closure__[0]



# c = f.__closure__[0].cell_contents

# c = make_cell(c)

# new = FunctionType(code=f.__code__, globals=f.__globals__, closure=(c,))

# print(new())
