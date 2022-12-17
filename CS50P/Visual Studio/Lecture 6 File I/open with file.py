name = input("What's your name? ")

with open("listofname.txt", "a") as file:
    file.write(f"{name}\n")