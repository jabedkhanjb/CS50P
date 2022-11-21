
i = 1
while i<=7:
    name = input("Pick a name of family members to see what they wanna be in future?\n> ").title().strip()
    match name:
        case "Preum" | "Jabed" | "Rahim" | "Ayaan":
            print("Engineer")
        case "Renu" | "Tanha":
            print("Doctor")
        case "Fahim" | "Kona":
            print("Business Administration")
        case _:
            print("Who?")
    i += 1