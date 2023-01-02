email = input("What's your email?\n").strip()

if "@" in email and "." in email:
    print(email,"is Valid")
else:
    print(f"{email} is Invalid")
    
EMAIL = input("What's your email address?\n").strip()

username, domain = EMAIL.split("@")

if username and "." in domain:
    print("Valid Email")
else:
    print("Invalid Email")