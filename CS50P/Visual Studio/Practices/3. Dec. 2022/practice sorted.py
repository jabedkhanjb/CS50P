names = []

with open("name_id.txt") as folder:
    for line in folder:
        # print(f"Hi, {line.rstrip()}")
#         print(line)
        names.append(line.rstrip())
        

for name in sorted(names):
    print(f"Hi, {name}")