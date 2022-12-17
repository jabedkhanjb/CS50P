name = []

for _ in range(5):
    name.append(input("What's your name? ").title())

for name in sorted(name):
    print(f"Hello, {name}")