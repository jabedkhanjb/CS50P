import re 

email = input("Enter your email: \n> ")

if re.search(r"^\w+@\w+\.(edu|com)$", email):
    print("Valid Email")
else:
    print("Invalid")