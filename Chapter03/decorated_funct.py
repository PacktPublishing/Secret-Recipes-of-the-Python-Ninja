@arg_check
def circle_measures(radius):
    circumference = 2 * pi * radius
    area = pi * radius * radius
    diameter = 2 * radius
    return (diameter, circumference, area)
