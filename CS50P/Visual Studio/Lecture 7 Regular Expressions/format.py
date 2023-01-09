name = input("What's your name?\n").strip()
if "," in name:
    last, first = name.split(",")
    name = f"{first} {last}"
print(f"Hello, {name}".title())