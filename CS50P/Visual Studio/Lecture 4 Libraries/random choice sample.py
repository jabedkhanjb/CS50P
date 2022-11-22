import random
shuffle = ["Head", "Tails"]
coin = random.choice(shuffle)
print(coin)

from random import sample
name = ["Jabed", "Renu", "Kona"]
coin = sample(name, 2)
for i in coin:
    print(i)
    
number = random.randint(2, 10)
print(number)

"Shuffles card"

card = ["King", "Queen", "Jack"]
random.shuffle(card)
for i in card:
    print(i)