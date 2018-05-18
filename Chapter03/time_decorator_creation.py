import time

def time_decorator(funct):
    def wrapper(*arg):
        # time = time.perf_counter()
        result = funct(*arg)
        print(time.perf_counter())
        return result
    return wrapper
