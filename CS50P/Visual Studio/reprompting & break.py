while True:
    try:
        x = int(input("Insert a value : "))
        print(f"Value is {x}")
    except ValueError:
        print("You haven't inserted an integer value.")
    else:
        break