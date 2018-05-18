def cor():
    hi = yield "Hello"
    yield hi
cor = cor()
print(next(cor))
print(cor.send("World"))
