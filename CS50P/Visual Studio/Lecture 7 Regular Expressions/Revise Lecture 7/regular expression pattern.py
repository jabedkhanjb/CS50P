import re

email = input("Input your email address: ").strip()

if re.search(".*@.+", email):
    print("Email is valid")
else:
    print("Email is invalid")