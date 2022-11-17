def main():
    x = get_int()
    print(f"Your given value is {x}")
    
def get_int():
    while True:
        try:
           return int(input("Insert value in y : "))
        except ValueError:
            print("This is not an integer.")

main()