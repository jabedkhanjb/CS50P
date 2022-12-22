email = input("What's your email?\n").strip()
"""
if "@" in email and "." in email:
    print("Valid Email")
    
else:
    print("Invalid Email Address")"""
    
username, domain = email.split("@")

"""if username and "." in domain:
    print("Valid")"""
if username and domain.endswith(".edu"):
    print("Valid")
    
else:
    print("Invalid")