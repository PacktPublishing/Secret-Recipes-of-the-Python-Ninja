In [8]: from collections import defaultdict

In [9]: age_groups = defaultdict(list)

In [10]: for person in people:
    ...:     age_groups[person.age].append(person)
    ...:     

In [11]: for k in age_groups:
    ...:     print(k, age_groups[k])
    ...:     
40 [40, 40]
18 [18, 18, 18]
42 [42]
25 [25]
23 [23]
80 [80]
67 [67]
