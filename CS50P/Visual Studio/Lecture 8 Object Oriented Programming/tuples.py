def main():
    # name = get_name()
    # house = get_house()
    # name, house = get_student()
    student = get_student()
    print(f"{student[0]} from {student[1]}".title())


# def get_name():
#     return input("Name: ").strip()

# def get_house():
#     return input("House: ").strip()

def get_student():
    name = input("Name: ").strip()
    house = input("HOuse: ").strip()
    # return name, house
    return (name, house)



if __name__ == "__main__":
    main()