>>> def first_func(val):
...     print(val)
...
>>> new_name = first_func
>>> first_func("Spam!")
Spam!
>>> new_name("Spam too!")
Spam too!
