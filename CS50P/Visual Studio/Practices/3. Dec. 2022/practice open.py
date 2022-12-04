name = input("Enter your name : ").title().strip()

folder = open("name_id.txt", "a")

folder.write(f"{name}\n")
folder.close()