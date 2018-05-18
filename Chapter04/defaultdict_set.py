>>> s = [("apple", 1), ("banana", 2), ("carrot", 3),  ("banana", 4), ("carrot", 1), ("banana", 4)]
>>> d = defaultdict(set)
>>> for k, v in s:
...     d[k].add(v)
...
>>> sorted(d.items())
[('apple', {1}), ('banana', {2, 4}), ('carrot', {1, 3})]
