def main():
    x = get_int("Enter a number: ")
    print(f"Here is the value of x in {x}")
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
main()
    