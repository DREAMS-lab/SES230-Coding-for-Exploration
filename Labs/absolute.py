def absolute(x):
    if x < 0:
        print("if block is running")
        return -x
    else:
        print("else block running")
        return x


print(absolute(0))