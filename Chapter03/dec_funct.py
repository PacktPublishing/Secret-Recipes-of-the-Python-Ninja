def arg_check(func):
    def wrapper(num):
        if type(num) != int:
            raise TypeError("Argument is not an integer")
        elif num <= 0:
            raise ValueError("Argument is not positive")
        else:
            return func(num)
    return wrapper
