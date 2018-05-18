for i in range(1000000, 0, -1):
    if i > 1:
        print("{} bottles of beer on the wall, {} bottles of beer.".format(i, i))
        if i > 2:
            additional = str(i - 1) + " bottles of beer on the wall."
    else:
        additional = "1 bottle of beer on the wall."
    if i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        additional = "no more beer on the wall!"
    print("Take one down, pass it around,{}\n".format(additional))
