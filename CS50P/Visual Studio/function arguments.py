def main():
    x = get_int("Hi Jb, What's x?\n> ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            pass
        
main()
