import math

# Silly little number cruncher
@time_decorator
def factorial_counter(x, y):
    fact = math.factorial(x)
    time.sleep(2)  # Force a delay to show the time decorator works
    fact2 = math.factorial(y)
    print(math.gcd(fact, fact2))

factorial_counter(10000, 10)
