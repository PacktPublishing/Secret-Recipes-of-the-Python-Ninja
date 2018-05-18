In [30]: student_grades = {}

In [31]: student_grades["Jeffrey"] = 98

In [32]: student_grades["Sarah"] = 85

In [33]: student_grades["Kim"] = 92

In [34]: student_grades["Carl"] = 87

In [35]: student_grades["Mindy"] = 98

In [36]: student_grades
Out[36]: {'Carl': 87, 'Jeffrey': 98, 'Kim': 92, 'Mindy': 98, 'Sarah': 85}

In [37]: sorted(student_grades.items(), key=lambda t: t[0])
Out[37]: [('Carl', 87), ('Jeffrey', 98), ('Kim', 92), ('Mindy', 98), ('Sarah', 85)]

In [38]: sorted(student_grades.items(), key = lambda t: t[1])
Out[38]: [('Sarah', 85), ('Carl', 87), ('Kim', 92), ('Jeffrey', 98), ('Mindy', 98)]

In [39]: sorted(student_grades.items(), key = lambda t: -t[1])
Out[39]: [('Jeffrey', 98), ('Mindy', 98), ('Kim', 92), ('Carl', 87), ('Sarah', 85)]

In [40]: rankings = collections.OrderedDict(sorted(student_grades.items(), key = lambda t: -t[1]))

In [41]: rankings
Out[41]: 
OrderedDict([('Jeffrey', 98),
             ('Mindy', 98),
             ('Kim', 92),
             ('Carl', 87),
             ('Sarah', 85)])
