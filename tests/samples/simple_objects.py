sample_dicts = [{1: 'a', 'asd': {True: 123, None: [{1.1: 'a'}, {}, 2, False]}},
                {'a': {'b': {1: 2}}},
                {'a': {'b': {}}},
                {'"a"""': 1, '"b"': 2, 'c"': [1, 2, complex(0, -3), 3]}
                ]

sample_lists = [[1, 2, complex(1, 2), 'qwe', None, True, False, [1, {'a': {1: True}}]],
                [[1, [2.2, 3], [4]]],
                [{}, [[[[]]]]]
                ]

sample_sets = [{1, 2, ('asd', True, False, tuple(), frozenset(['qwe', 1, None]))},
               {'qwe', None, tuple(tuple(['HAHAHAHA', 1, 2, 3, False]))}
               ]

single_primitives = [1, 1.2, True, False, None, 'HAHA', complex(1, 1.2)]


sample_bins = [bytes([1, 2, 3, 2]),
               bytearray('LOLOLOLOLOLOLO', encoding='utf-8')
               ]


# recursion samples
recursion_a = {'a': 1, 'b': {'a': False, 'n': True, 1: None, 'm':
                             {'l': [], 'v': 'nooo', 'n': {}}}, 'o': 123.12, 'f': tuple(), 'g': set()}

recursion_b = {'a': [1, 2, 3, [], []]}

recursion_c = [1, 2, 3, {'a': {}}]

recursion_d = [1, {'a': [4, {'b': False}, 5]}, 1]

recursion_e = [1, 2, {'a': [1, 2, 3], 'b': [
    4, 'qwe', None]}, {'b': {'a': 'hello'}}]

recursion_f = []

recursion_g = {'a':
               {'c': 'qwe',
                'g': {'l': [1, {'a': 'hello', 'b': 'hi'}, 3]}
                },
               'b':
               {'f': [1, 2, 3],
                   'b': False,
                   'c': True,
                   'n': None
                }
               }

recursion_h = [[1, 2, 3], [1, [2, [4, [5], 6]]], [7, 8, [9]]]

recursion_i = [{'a': 123, 'b': 666}, 'qwe', False, True, ['hello', None]]

test_recursion = [recursion_a,
                  recursion_b,
                  recursion_c,
                  recursion_d,
                  recursion_e,
                  recursion_f,
                  recursion_g,
                  recursion_h,
                  recursion_i]
