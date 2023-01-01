import re
    # """
    # re.IGNORECASE
    # re.MULTILINE
    # re.DOTALL
    # """
email = input("Enter your email address: ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    # by using re.IGNORECASE, it ignores whether the email 
    # address is in upper case or lower case.
    print("This is a valid email")
else:
    print("This is a invalid email")