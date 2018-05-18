>>> c = Counter()
>>> c['a'] += 1
>>> len(c)
1
>>> c['a'] -= 1
>>> len(c)
1
>>> c['a'] += 2
>>> len(c)
1
>>> len(Counter('aaabbc'))
3
>>> b = bag()
>>> b.add('a')
>>> len(b)
1
>>> b.remove('a')
>>> len(b)
0
>>> len(bag('aaabbc'))
6
