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
    for tanha in range(n):
        print(f"Kitten number {tanha}")
        
        
        
main()