import sys

if len(sys.argv) < 15:
    print("There are too few arguments.")
elif len(sys.argv) > 5:
    print("There are too many arguments.")
else:
    print("Hello, my name is", sys.argv[1])
    
"""Let's modify the following code above"""
# check for errors 
if len(sys.argv) < 2:
    print("Only few arguments.")
elif len(sys.argv) > 2:
    sys.exit("Most of the arguments.")

# print name tags
print("Hello, my name is", sys.argv[1])