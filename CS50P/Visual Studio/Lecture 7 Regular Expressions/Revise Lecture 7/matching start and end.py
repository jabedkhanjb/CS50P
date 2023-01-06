import re 

email = input("Please, insert your email : ")

if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.edu$", email):
    # by using "^[^@]+@[^@]+\.edu$" this command it will
    # stop counting extra @ sign over here except one as a valid 
    # email, and the output will be invalid for sure for the redundancy of @ sign
    print("Completely Valid")
else:
    print("Mysteriously invalid")
    
    # depressed