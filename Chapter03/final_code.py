from math import pi 

def arg_check(func):
    def wrapper(num):
        if type(num) != int:
            raise TypeError("Argument is not an integer")
        elif num <= 0:
            raise ValueError("Argument is not positive")
        else:
            return func(num)
    return wrapper

@arg_check
def circle_measures(radius):
    circumference = 2 * pi * radius
    area = pi * radius * radius
    diameter = 2 * radius
    return (diameter, circumference, area)

diameter, circumference, area = circle_measures(6)
print("The diameter is", diameter, "\nThe circumference is", circumference, "\nThe area is", area)
