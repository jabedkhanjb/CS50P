import re

email = input("Please, provide us your email address to check if it is valid: \n")
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
if re.search(r"^[a-zA-Z0-9_\.]+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("VALID EMAIL")
else:
    print("INVALID EMAIL")