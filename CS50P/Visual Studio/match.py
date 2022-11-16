name = input("What's your name? ").title().strip()

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
# elif name == "Hermione":
#     print("Leonardo")
# elif name == "Ron":
#     print("Slytherin")
else:
    print("Who? ")
    
print("Code Match")

name  = input("What's your name? ").title().strip()

match name:
    case "Harry" | "hermione" | "Ron":
        print("Match name Matched")
    # case "Hermione":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")