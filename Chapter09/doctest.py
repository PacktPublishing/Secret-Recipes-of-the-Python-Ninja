"""
Factorial module.

This module manually defines the factorial() function (ignoring the fact that Python includes math.factorial().  For example,

>>> factorial(4)
24
"""

def factorial(n):
    """Return the factorial of n.

	Normal loop
    >>> for n in range(4): print(factorial(n))
    1
    1
    2
    6
	
	List comprehension
	>>> [factorial(n) for n in range(6)]
        [1, 1, 2, 6, 24, 120]
	
	Normal factorial
    >>> factorial(25)
    15511210043330985984000000

	Negative check
    >>> factorial(-3)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Float must be an exact integer:
    >>> factorial(25.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(25.0)
    15511210043330985984000000

    It must also not be ridiculously large:
    >>> factorial(1e25)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e100
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    print(doctest.__file__)
    doctest.testmod()
