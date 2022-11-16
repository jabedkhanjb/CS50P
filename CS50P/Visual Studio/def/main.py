from re import X


def main():
    x = int(input("What's X? "))
    print("x squared is", squre(x))


def squre(n):
    return pow(n, 3)


main()