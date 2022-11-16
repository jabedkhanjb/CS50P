def main():
    print_star(3)
    

def print_star(x):
    for i in range(x):
        for j in range(15):
            print("_", end="")
        print("")
        

main()