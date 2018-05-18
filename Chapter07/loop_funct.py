from file1 import add

def loop():
    i = 0
    a = 0.0
    while i < 1000000000:
        a += 1.0
        add(a, a)
        i += 1

if __name__ == "__main__":
    loop()
