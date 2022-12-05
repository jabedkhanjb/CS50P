names = []

with open("name_id.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names, reverse=True):
    print(f"hello, {name}")