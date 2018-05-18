>>> from collections import UserList
>>> class ExtendList(UserList):
...     def __setitem__(self, i, value):
...             if i == len(self.data):
...                     self.data.append(value)
...             else:
...                     self.data[i] = value
... 
>>> l = ExtendList()
>>> for i in range(10):
...     l[i] = i
... 
>>> print(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[10] = 10
>>> print(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l[2] = 43
>>> print(l)
[0, 1, 43, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l[12] = 46
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __setitem__
IndexError: list assignment index out of range
