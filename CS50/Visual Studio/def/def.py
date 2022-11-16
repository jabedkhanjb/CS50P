from turtle import title


def hello(to = "World"): # def(function), hello(function name), (x,y)is called function parameter
    print("Hello,", to)

hello()
name = input("What's your name? ").strip().title()
hello(name)
