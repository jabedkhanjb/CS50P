x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y
print(z)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y) # to get a round shape number with maximum probability
print(f"{z:,}") # to get , comma in numbers

x = float(input("What's x? "))
y = float(input("What's y? "))

# z = round(x / y, 3) one method
z = round(x / y) 
print(f"{z:.2f}") 