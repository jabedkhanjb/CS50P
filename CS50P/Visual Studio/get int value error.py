def main():
    x = get_int()
    print(f"Our value x is {x}")
    

def get_int():
    while True:
        try:
            x = int(input("What's x?\n> "))
        except ValueError:
            print("X is not an integer.")
        else:
            break
    return x

main()