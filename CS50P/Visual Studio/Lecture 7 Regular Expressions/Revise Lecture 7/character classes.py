import re 

email = input("Please, insert your email : ")
if re.search(r"^\w+@[a-zA-Z0-9_.]+\.edu$", email):
    # backslash w in this case represents a "word character"
    # which is commonly known as a alphanumeric symbol or the underscore
    print("This email is Valid")
else:
    print("This email is Invalid")
    