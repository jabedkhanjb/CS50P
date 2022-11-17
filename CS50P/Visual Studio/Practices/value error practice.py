# infinity question asking until get the right below

while True:
    try:
        x = int(input("What's x?\n> "))
        print(f"Your given number is {x}")
    except ValueError:
        print("x is not an integer.")
    else:
        break

    """
    this loop will be happening 5 times until the user input is not an integer value.
    also, it shows how many attempts the user takes
    """
i = 1
while i <= 5:
    try:
        x = int((input("Enter an integer value: ")))
        print(f"You have inputted {x}")
    except ValueError:
        print("x is not integer.")
        if i == 1:
             print(f"{i}st attempt failed.")
        elif i <= 3:
            print(f"{i}nd attempt failed.")
        else:
            print(f"{i}th attempt failed.")
    i += 1
        
        
        