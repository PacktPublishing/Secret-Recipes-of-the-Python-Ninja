import math

TIMES = 10000000
a = 1
b = 1

for i in range(TIMES):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    a += 1
    b += 2
