with open("name_list.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print(f"Hello, {line.rstrip()}")
    
"""Second way of shortcut"""

with open("listofname.txt", "r") as file:
    for line in file:
        print(f"Hi, {line.rstrip()}")