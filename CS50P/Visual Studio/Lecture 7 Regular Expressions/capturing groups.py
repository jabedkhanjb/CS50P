import re
name = input("What's your name?\n").strip()

match = re.search(r"^(.+), *(.+)$", name)
if match:
    # last, first = match.groups()
    # name = f"{first} {last}"
    name = match.group(2) + " " + match.group(1)
print(f"Hello, {name}".title())