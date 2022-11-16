def main():
    x = get_int()
    print(f"Here is the value of x in {x}")
    
def get_int():
    while True:
        try:
            return int(input("Hey, What's the value of x?\n> "))
        except ValueError:
            pass
        
main()
    