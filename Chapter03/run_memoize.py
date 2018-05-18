import time

@memoize
def data_simulator():
    time.sleep(2)
    return "done"
