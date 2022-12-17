students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
        
        
def get_name(student):
    return student["house"]

for student in sorted(students, key=get_name, reverse=True): 
    """Using 'reverser=True' will resorted the value over here.
    and if we don't use this formula/method, we will get a 
    sorted list of dictionary."""
    print(f"{student['name']} is in {student['house']}")