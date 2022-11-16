i = 3
while i != 0:
    print("Loop is successful.")
    i = i - 1
    
# another way in while loop

print("\n")

i = 1
while i <= 6:
    print("This is While loop")
    i+=1
    
# an way to ask question that the number of input and then print
i = int(input("Enter the number of loops: \n> "))
while i != 0:
    print(f"Nice Loop {i}")
    i-=1
    
# one more way 
i = 1
a = int(input("Enter the number of index: "))
while i <= a:
    print(f"Multiple loops counting from number {i}")
    i += 1
    