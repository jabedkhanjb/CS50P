name = []

for _ in range(5):
    name.append(input("What's your name? ").title().strip())


for nlist in sorted(name):        
    print(nlist)