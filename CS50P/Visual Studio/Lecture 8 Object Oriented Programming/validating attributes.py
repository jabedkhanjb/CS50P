# import sys

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Dhaka", "Chittagong", "Lakshmipur"]:
            raise ValueError("Invalid House")
            # return None
            # sys.exit("Missing name")
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    
     
    
    
if __name__ == "__main__":
    main()
    