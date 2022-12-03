name = input("What's your name? ").title()

# file = open("information.txt", "w")
file = open("information.txt", "a")

"""
    w for write
    a for append
   
"""
file.write(f"{name}\n")
file.close()