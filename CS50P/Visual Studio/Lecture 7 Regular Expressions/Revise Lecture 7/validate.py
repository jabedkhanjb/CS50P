email = input("What's your email?\n").strip()

if "@" in email and "." in email:
    print("\nYour email address",'"'+email+'"',"is Valid")
else:
    print("\nYour email address",'"'+f"{email}"+'"', "is Invalid")
    
EMAIL = input("What's your email address?\n").strip()

username, domain = EMAIL.split("@")
print("Here is your username", username)
if username and "." in domain:
    print("Valid Email")
else:
    print("Invalid Email")
    
mail = input("Insert your email address: ")

uname, dname = mail.split("@")

if uname and dname.endswith(".edu"):
    print("Good Result")
else:
    print("Bad Result")