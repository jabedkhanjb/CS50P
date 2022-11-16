name = input("What's your name? \n").title().strip()

match name:
    case "Jabed":
        print("Name matched.")
    case "Renu":
        print(f"This is {name}")
    case "Kona":
        print("Kona is matched.")
    case _:
        print(f"Who is {name}? ")