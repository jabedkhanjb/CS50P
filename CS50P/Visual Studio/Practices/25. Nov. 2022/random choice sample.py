import random
shuffle = ["Head", "Tails", "Draw"]
coin = random.choice(shuffle)
print(coin)

name = ["Alex", "Tailors", "Britney", "Alen"]

pick_a_name = random.sample(name, 2)


print("***********************************")
print("***        Pick two name        ***")
print("***********************************")
for i in pick_a_name:
    print(i)
    
    

print("Random names are : ")
for i in pick_a_name:
    if i == "Tailors":
        continue
    print(i)
    
    
"""Shuffle the card"""

print("\nLet's shuffle the card : ")
card = ["King", "Queen", "Jack", "Witch"]

random.shuffle(card)
for i in card:
    print(i)
