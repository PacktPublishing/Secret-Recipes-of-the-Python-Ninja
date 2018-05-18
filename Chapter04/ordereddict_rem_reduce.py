>>> del OrderedCounter.__reduce__ 
>>> copy.copy(oc) 
OrderedCounter(OrderedDict([('b', 2), ('a', 5), ('c', 1), ('r', 2), ('d', 
1)])) 
