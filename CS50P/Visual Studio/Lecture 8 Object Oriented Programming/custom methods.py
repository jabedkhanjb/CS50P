class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Dhaka", "Chittagong", "Lakshmipur"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def Charm(self):
        match self.patronus:
            case "UK":
                return "🙂"
            case "Canada":
                return "😮"
            case "USA":
                return "🥳"
            case "Bangladesh":
                return "🥺"
            case _:
                return "Don't Worry"
            
    
def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.Charm())
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
    
     
    
    
if __name__ == "__main__":
    main()
    