import math

TIMES = 10000000
a = 1
b = 1

def calcMath(i, a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

for i in range(TIMES):
    c = calcMath(i, a, b)
    a += 1
    b += 2
