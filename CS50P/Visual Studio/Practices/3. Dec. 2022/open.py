name = input("What's your name? ")

# file = open("information.txt", "w")
file = open("information.txt", "a")

"""
    w for write
    a for append
   
"""
file.write(name)
file.close()