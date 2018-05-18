>>> def func_creator():
...     def return_saying():
...         return "Blessed are the cheese makers"
...     return return_saying
... 
>>> statement = func_creator()
>>> print(statement())
Blessed are the cheese makers
