import re

email = input("What's your academic email address?\n").strip()

"""
1) .    any character except a new line
2) *    0 or more repetitions
3) +    1 or more repetitions
4) ?    0 or 1 repetition
5) {m}  m repetitions
6) {m,n}    m-n repetitions
"""

# single dot "." means any character, and dot-star ".*" means
# zero or more other characters or only plus "+" is the alternative
# of dot-star ".*" which express the same. 
if re.search(r".+@.+", email):
    print("This is a Valid Email")
else:
    print("This is an Invalid Email")