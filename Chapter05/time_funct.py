import statistics

times = []

def avg_time(func, val):
	for num in range(val):
		times.append(func)
	return statistics.mean(times)
