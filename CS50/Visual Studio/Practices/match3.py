name = input("What's your name? \n> ").title().strip()
match name:
    case "Tanha": 
        print(f"{name} is a Daughter of Taiyub Ullah.")
    case "Ayaan": 
        print(f"{name} is a Son of Sabarin Chowdhury Mou.")
    case "Renu" | "Kona":
        print(f"{name} is a Daughter of Mahbub Islam Khan Parvez.")
    case "Jabed":
        print(f"{name} is the only Son of Jobeda Khatun.")
    case _:
        print("Who? ")
    