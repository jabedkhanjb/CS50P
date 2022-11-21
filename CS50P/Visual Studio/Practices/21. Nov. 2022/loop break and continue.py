name = input("Enter your name : ").strip()
target = input("Put your targetted letter : ").strip()
print(name)
for i in name:
    if i == target:
        break
    # after this line, execution would be terminated
    print(i, end="")
print(f"\nLoop terminated when '{i}' was found in the name.")        

"""When we will use continue, execution will be continuing except that condition in entire process"""

name = input("Enter name : ").strip()
target = input("Put your targetted clause of the name : ")
    
for i in name:
    if i == target:
        continue
    print(i, end="")
print(f"\nName has been printed except '{target}'")

    