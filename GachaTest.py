import random as rand

pool = {
    "Legendary": .6,
    "Exotic": 5,
    "Rare": 15,
    "Uncommon": 25,
    "Common": 54.4,
}

TotalWeight = 0
for rarity in pool:
    pool[rarity] *= 10
    chances = pool[rarity]

    TotalWeight += chances

for i in range(10):
    keyNum = rand.randint(0,int(TotalWeight))
    weight = 0

    for rarity in pool:
        chances = pool[rarity]
        weight += chances

        if keyNum <= weight:
            print(rarity)
            break