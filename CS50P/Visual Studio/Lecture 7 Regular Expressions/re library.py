import re

email = input("What's your email address?\n").strip()


"""
1) .    any character except a new line
2) *    0 or more repetitions
3) +    1 or more repetitions
4) ?    0 or 1 repetition
5) {m}  m repetitions
6) {m,n}    m-n repetitions
"""
"""
^ matchs the start of the string
$ matches the end of the string or just before the newline
  at the end of the string

"""

if re.search(r".+@.+\.edu$", email): # r refers to raw string, f stands for format string
    print("Valid")
else:
    print("Invalid")