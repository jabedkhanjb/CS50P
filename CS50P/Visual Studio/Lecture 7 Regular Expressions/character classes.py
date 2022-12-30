import re

email = input("Hey, input your email address: \n").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid Email")
else:
    print("Invalid Email")
    
    """
    reference to character classes
\d  decimal digit 
\D  not a decimal digit
\s  whitespace characters 
\S  not a whitespace character
\w  word character ... as well as numebers and the underscore 
\W  not a word character 
    
    """