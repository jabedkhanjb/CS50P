name = input("Insert your name : ").title().strip()

with open("name_id.txt", "a") as drive:
    drive.write(f"{name}\n")
    drive.close()