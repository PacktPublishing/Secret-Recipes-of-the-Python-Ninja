>>> from collections_extended import setlist
>>> import string
>>> sl = setlist(string.ascii_lowercase)
>>> sl
setlist(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'))
>>> sl[3]
'd'
>>> sl[-1]
'z'
>>> 'r' in sl   # testing for inclusion is fast
True
>>> sl.index('m')       # so is finding the index of an element
12
>>> sl.insert(1, 'd')   # inserting an element already in raises a ValueError
Traceback (most recent call last):
...
        raise ValueError
ValueError
>>> sl.index('d')
3
