>>> def greeting(name):
...     return "'allo " + name
...
>>> def call_me(func):
...     nickname = "mate"
...     return func(nickname)
... 

>>> print(call_me(greeting))
'allo mate
