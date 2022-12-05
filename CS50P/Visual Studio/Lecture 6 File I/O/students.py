with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        
print("\nNew Code\n")
student = []

with open("names.csv") as folder:
    for line in folder:
        name, house = line.rstrip().split(",")
        students = {"name" : name, "address" : house}
        # students["name"] = name
        # students["address"] = house
        student.append(students)
        
for info in sorted(student):
    print(f"{info['name']} is in {info['address']}")