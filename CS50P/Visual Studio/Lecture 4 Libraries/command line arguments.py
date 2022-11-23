import sys


if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])

"""Modify the following code above"""

import sys
# check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# print name tags
print("Hello, my name is", sys.argv[1])


