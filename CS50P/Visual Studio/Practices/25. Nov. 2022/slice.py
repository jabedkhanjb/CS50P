import sys
if len(sys.argv) < 2:
    sys.exit("There are two few arguments.")
    
for arg in sys.argv[1:-2]:
    print("Hello, My name is", arg)