import re

email = input("Hey, input your email address: \n").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid Email")
else:
    print("Invalid Email")