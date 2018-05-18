In [3]: age_groups = {}

In [4]: for person in people:
   ...:     age = person.age
   ...:     if age in age_groups:  # does the age already exist in the dictionary?
   ...:         age_groups[age].append(person)  # if so, append a new item
   ...:     else:
   ...:         age_groups[age] = [person]  # add the age value to the dictionary
   ...:         

In [5]: for i in age_groups:
   ...:     print(i)
   ...:     
40
18
42
25
23
80
67

In [6]: age_groups.items()
Out[6]: dict_items([(40, [40, 40]), (18, [18, 18, 18]), (42, [42]), (25, [25]), (23, [23]), (80, [80]), (67, [67])])

In [7]: for k in age_groups:
   ...:     print(k, age_groups[k])
   ...:     
40 [40, 40]
18 [18, 18, 18]
42 [42]
25 [25]
23 [23]
80 [80]
67 [67]
