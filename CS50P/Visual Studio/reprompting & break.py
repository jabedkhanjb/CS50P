"""This is repromting code"""
while True:
    try:
        x = int(input("Insert a value : "))
        # print(f"Value is {x}")
    except ValueError:
        print("You haven't inserted an integer value.")
    else:
        break
print(f"Value is {x}")


"""This is break code"""

while True:
    try:
        x = int(input("Push a value into x = "))
        break
    except ValueError:
        print("This is not an integer value.")

print(f"Here is your value x = {x}")