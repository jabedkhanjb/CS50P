import re

email = input("Hey, input your email address: \n").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid Email")
else:
    print("Invalid Email")