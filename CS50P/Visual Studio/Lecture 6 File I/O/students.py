with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        
print("\nNew Code\n")
student = []

with open("names.csv") as folder:
    for line in folder:
        name, house = line.rstrip().split(",")
        student.append(f"{name} is in {house}")
        
for students in sorted(student):
    print(students)