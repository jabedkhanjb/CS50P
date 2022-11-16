for i in [0, 1, 2]:
    print("Hello World")
    
print("\n")

for i in range(8):
    print("Hey, How are you doing? ")
    
print("\n")

print("Hello Jabed \n" * 5, end="")

print("\n")

while True:
    n = int(input("What's n? \n> "))
    if n > 0:
        break
for i in range(n):
    print(f"Meow number {i}")
    
print("\n def function looping system\n")

def main():
    number = get_number()
    animal(number)
    
def get_number():
    while True:
        j = int(input("What's the number? \n:- "))
        if j > 0:
            break
    return j
    

def animal(j):
    for i in range(j):
        print(f"def Loop which is amazing {i}")
    
main()
