# print("#\n" * 3, end="")
print("Vertical #\n")

def main():
    print_column(5)

def print_column(height):
    for _ in range(height):
        print("#")
        
main()

print("Horizontal *\n")

def main():
    value = int(input("What's row? \n> "))
    print_row (value)
    
def print_row(width):
    print("*" * width)

main()

print("Squre")

def main():
    print_squre(3)
    
def print_squre(size):
    for i in range(size):
        for j in range(size):
            print("^^^^^^^^^^^^^^^", end="")
        print("")
        
main()

print("Alternative of previous code\n")

def main():
    print_squre(3)
    
    
def print_squre(size):
    for i in range(size):
        row(size)
    
def row(width):
    print("+" * width)
    
main()


