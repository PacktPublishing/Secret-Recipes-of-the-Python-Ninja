>>> from collections_extended import bijection
>>> bij = bijection({'a': 1, 'b': 2, 'c': 3})
>>> bij.inverse[2]
'b'
>>> bij['a'] = 2
>>> bij == bijection({'a': 2, 'c': 3})
True
>>> bij.inverse[1] = 'a'
>>> bij == bijection({'a': 1, 'c': 3})
True
