i = 3
while i != 0:
    print(f"Loop is Successful {i}")
    i -= 1

print("\nAnother way \n")

i = 1
while i < 6:
    print(f"Another Loop is Successful {i}")
    i += 1
    
print("\nOne more way \n")

i = int(input("How many times would you like to process the loop? \n> "))
while i != 0:
    print(f"Process the Loop {i}")
    i -= 1
    
print("\nLast way \n")

i = 1
x = int(input("How long will the loop process? \n> "))
print(f"Execution begin from {i}")
while i < x:
    print(f"Process number {i}")
    i += 1
print(f"Executed to the number of {x}")