print("\nBasic way of printing Even Odd Number.\n")
x = int(input("What's X?\n> "))

if x % 2 == 0:
    print(f"{x} is an Even number")

else:
    print(f"{x} is an Odd number")

print("\nComplicated way of printing Even Odd Number. \n")

def main():
    x = int(input("What's the number of X?\n> "))
    if x_number(x):
        print(f"{x} is an Even Number.")
    else:
        print(f"{x} is an Odd Number.")
        
def x_number(x):
    return x % 2 == 0

main()