try:
    x = int(input("Enter the value of x?\n> "))
    print(f"The number you have inputted is {x}")
except ValueError:
    print("This is not an integer.")

# else condition

try:
    y = int(input("Insert a value : "))
except ValueError:
    print("This value is not recognised as an integer.")
else:
    print(f"Value is {y}")