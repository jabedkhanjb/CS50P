names = []

with open("name_id.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello, {name}")