def fun_decorator(some_funct):
    def wrapper():
        print("Here is the decorator, doing its thing")
        for i in range(10):
            print(i)
        print("The decorator is done, returning to the originally scheduled function")
        print(some_funct())
    return wrapper

def a_funct():
    text = "I am the original function call"
    return text

a_funct = fun_decorator(a_funct)
a_funct()
