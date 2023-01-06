import re 
email = input("Hey, what's your email address: ").strip().lower()
if re.search(r"^[a-zA-Z0-9_. ]+@[a-zA-Z0-9_. ]+\.edu", email):
    print("Valid")
else:
    print("Invalid")

gmail = input("Hey, what's your email address: ").strip().lower()
if re.search(r"^(\w|\s)+@(\w|\s)+\.(edu|govt|us|bd|org|net)", gmail):
    print("This email is valid")
else:
    print("Unfortunetly this email is invalid")
    
    