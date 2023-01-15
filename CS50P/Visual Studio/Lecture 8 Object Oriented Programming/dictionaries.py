def main():
    student = get_student()
    if student["name"] == "Jabed":
        student["house"] = "USA"
    print(f"{student['name']} from {student['house']}")
    
    
def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name: ").title()
    house = input("House: ")
    return {"name" : name, "house" : house}


if __name__ == "__main__":
    main()