>>> def print_input(*args):
...   for val, input in enumerate(args):
...       print("{}. {}".format(val, input))
...
>>> print_input("spam", "spam", "eggs", "spam")
0. spam
1. spam
2. eggs
3. spam
