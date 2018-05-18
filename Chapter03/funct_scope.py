>>> def func_creator2(name):
...     def greeting():
...         return "Welcome, " + name
...     return greeting
... 
>>> greet = func_creator2("Brian")
>>> print(greet())
Welcome, Brian
