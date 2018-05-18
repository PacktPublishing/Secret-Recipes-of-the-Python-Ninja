>>> l = [[3, 56], [2, 34], [6, 98], [1, 43]]
>>> def diffSort(item):
...     return item[1]
... 
>>> l.sort(key=diffSort)
>>> l
[[2, 34], [1, 43], [3, 56], [6, 98]]
