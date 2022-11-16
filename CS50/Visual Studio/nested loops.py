# vertical
def main():
    print_column(3)
    
    
def print_column(height):
    for _ in range(height):
        print("#")
        
        
main()

# horizontal
def main():
    print_row(4)
    
    
def print_row(width):
    print("?" * width)
    

main()

# squre
def main():
    print_square(3)
    
# for each row in square
def print_square(size):
    for i in range(size):
        
        # for each brick in row
        for j in range(size):
            
            # print brick
            print("###", end="")
        print()
    
    
main()

# Alternative of squre
def main():
    print_square(3)
    
# for each row in square
def print_square(size):
    for i in range(size):
        print_row(size)
       
       
def print_row(width):
    print("#*#" * width)
    
    
main()