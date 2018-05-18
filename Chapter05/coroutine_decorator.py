def coroutine(funct):
	def wrapper(*args, **kwargs):
		cor = funct(*args, **kwargs)
		next(cor)
		return cor
	return wrapper
