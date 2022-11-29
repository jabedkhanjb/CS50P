def main():
    """What if we remove 'int' over here"""
    # x = int(input("Insert the value of X : "))
    x = input("Enter a number : ")
    print("x squred is", square(x))
    
    
def square(i):
    return i * i


if __name__ == "__main__":
    main()