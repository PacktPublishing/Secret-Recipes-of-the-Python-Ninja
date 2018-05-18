>>> from collections import UserString
>>> class AppendString(UserString):
...     def append(self, s):
...             self.data = self.data + s
... 
>>> s = AppendString("abracadabra")
>>> s.append("spam and bananas")
>>> print(s)
abracadabraspam and bananas
>>> l = "banana"  # show that regular strings don't have an append method
>>> l.append("apple")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
