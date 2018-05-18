def my_generator(x):
    while x:
        x -= 1
        yield x

mygen = my_generator(5)
next(mygen)  # continue until iteration stops

