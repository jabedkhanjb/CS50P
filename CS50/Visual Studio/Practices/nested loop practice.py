def main():
    size(3)

def size(x):
    for i in range(x):
        row(x)
        
        
def row(n):
    print("****" * n)
    
main()

# another way to print this same line
print("New for loop")

for i in range(3):
    for j in range(12):
        print("*", end="")
    print("")
    
def main():
    printing_size(3)
    
def printing_size(size):
    for i in range(size):
        for j in range(75):
            print("$", end="")
        print("")
        
main()
    