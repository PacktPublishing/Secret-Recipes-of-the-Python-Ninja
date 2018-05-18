>>> c = Counter(a=2, b=-4)
>>> +c	# removes negative and zero values
Counter({'a': 2})
>>> -c	# inverts signs; negative values are ignored
Counter({'b': 4})
