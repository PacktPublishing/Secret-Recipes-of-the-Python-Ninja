import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))
