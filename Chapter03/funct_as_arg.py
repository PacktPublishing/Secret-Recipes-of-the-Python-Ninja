>>> def mult(x, y):
...     return x * y
... 
>>> def div(x, y):
...     return x / y
... 
>>> def math(func, x, y):
...     result = func(x, y)
...     return result
... 
>>> math(mult, 4, 2)
8
>>> math(div, 4, 2)
2.0
