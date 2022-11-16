for i in [0, 1, 2]:
    print("Meow")

for i in range(3):
    print(f"Meow {i}")
    
print("Cat \n" * 4, end="")

while True:
    n = int(input("What's n? \n> "))
    if n > 0:
        break

for i in range(n):
    print(f"Meow {i}")
    
    
# def function looping system    
print("\nLoop using function call\n")

def main():
    number = get_number()
    animal(number)
    

def get_number():
    while True:
        n = int(input("What's n? \n> "))
        if n > 0:
            break
    return n

def animal(n):
    for _ in range(n):
        print("Kitten")
        
main()