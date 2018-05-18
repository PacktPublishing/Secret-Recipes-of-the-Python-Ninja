>>> def person(name):
...     def greeting():
...         return "Would you like some spam, "
...     greet = greeting() + name + "?"
...     return greet
... 
>>> print(person("Sir Galahad"))
Would you like some spam, Sir Galahad?
