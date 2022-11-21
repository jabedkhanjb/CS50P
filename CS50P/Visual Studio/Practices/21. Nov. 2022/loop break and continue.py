name = input("Enter your first name : ").strip()
target = input("Put your targetted letter : ").strip()
print(name)
for i in name:
    if i == target:
        break
    print(i, end="")
print(f"\nLoop terminated when '{i}' was found in the name.")        