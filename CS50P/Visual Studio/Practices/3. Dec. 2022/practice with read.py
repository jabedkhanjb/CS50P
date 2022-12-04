with open("name_id.txt", "r") as folder:
    lines = folder.readlines()
    
for line in lines:
    # print("Hello,", line, end="")
    # print(f"Hello, {line}", end="")
    print(f"Hello, {line.rstrip()}")