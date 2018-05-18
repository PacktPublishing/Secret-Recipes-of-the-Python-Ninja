>>> count["bacon"] = 0	# assigning a value of 0 to "bacon"
>>> count
Counter({'spam': 1, 'eggs': 1, 'bacon': 0})
>>> del count["bacon"]	# del must be used to actually remove "bacon"
>>> count
Counter({'spam': 1, 'eggs': 1})
