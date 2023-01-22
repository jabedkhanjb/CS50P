import random

class Hat:
    
    houses = ["Dhaka", "Chattogram", "Lakshmipur"]
        
    @classmethod    
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    
    
Hat.sort(input("> "))