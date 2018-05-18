from collections import deque
import itertools

def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)  # create an iterable object from input argument
    d = deque(itertools.islice(it, n-1))  # create deque object by slicing iterable
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n  # yield is like "return" but is used with generators

ma = moving_average([40, 30, 50, 46, 39, 44])
next(ma)
next(ma)
next(ma)
