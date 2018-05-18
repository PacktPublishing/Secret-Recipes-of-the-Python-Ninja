>>> from collections import ChainMap
>>> x = {"a": 10, "b": 20}
>>> y = {"b": 30, "c": 40}
>>> z = ChainMap(y, x)
>>> for key, value in z.items():
...     print(key, value)
... 
a 10
b 30
c 40
>>> z = ChainMap(x, y)
>>> for key, value in z.items():
...     print(key, value)
... 
a 10
b 20
c 40
