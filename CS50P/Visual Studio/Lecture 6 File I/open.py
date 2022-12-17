name = input("What's your name? ")

file = open("name_list.txt", "a")
file.write(f"{name}\n")
file.close()