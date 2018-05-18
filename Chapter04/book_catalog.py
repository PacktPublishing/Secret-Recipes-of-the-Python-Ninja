In [1]: import collections

In [2]: bookCatalog = collections.defaultdict(lambda:"Unavailable")

In [3]: bookCatalog["a"] = "Arts"

In [4]: bookCatalog["b"] = "Biology"

In [5]: bookCatalog["c"] = "Chemistry"

In [6]: bookCatalog["d"] = "Dentistry"

In [7]: print(bookCatalog)
defaultdict(<function <lambda> at 0x7f41ab5f3840>, {'a': 'Arts', 'b': 'Biology', 'c': 'Chemistry', 'd': 'Dentistry'})

In [8]: for k in bookCatalog:
   ...:     print(k, bookCatalog[k])
   ...:     
a Arts
b Biology
c Chemistry
d Dentistry

In [9]: bookCatalog["z"]
Out[9]: 'Unavailable'

In [10]: for k in bookCatalog:
    ...:     print(k, bookCatalog[k])
    ...:     
a Arts
b Biology
c Chemistry
d Dentistry
z Unavailable
