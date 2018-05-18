>>> from collections import OrderedDict
>>> d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}  # regular unsorted dictionary

>>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))  # dictionary sorted by key
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

>>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))  # dictionary sorted by value
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

>>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))  # dictionary sorted by length of the key string
OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])
