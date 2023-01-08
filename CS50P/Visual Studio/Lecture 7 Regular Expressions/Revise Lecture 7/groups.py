import re
email = input("What's your email?\n").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
    
    # ? represents that 0 or 1 repetition
    # line number 4: instead of ^(\w|\.), can use [a-z0-9_\.] if use re.IGNORECASE
    # . means any character like */-+\';=-0, so for specific . in email address
    #       use \. mean we are only seeking . 
    