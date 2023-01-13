import re

email = input("Enter your email: ").strip()

if re.search(r"^\w.+@\w+\.(\w+\.)?(edu|com)$", email):
    print("Valid Email")
else:
    print("Invalid Email")