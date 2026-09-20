import random as rand
from colorama import init, Fore
init(autoreset=True)

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

def gacha():
    while True:
        try:
            gachaType = int(input(Fore.CYAN + """Pick gacha method:
[1] Single Pull
[2] 10x Pull
Input: """))

            if gachaType not in [1,2]:
                print(Fore.RED + "ERROR: Please input either 1 or 2!")
                continue
            
        except ValueError:
            print(Fore.RED + "ERROR: Input a valid value!")
            continue
        break

    print("="*50)

    if gachaType == 1:
        keyNum = rand.randint(0,int(TotalWeight))
        weight = 0
        
        for rarity in pool:
            chances = pool[rarity]
            weight += chances
        
            if keyNum <= weight:
                return [rarity]
    else:
        result = []

        for i in range(10):
            keyNum = rand.randint(0,int(TotalWeight))
            weight = 0

            for rarity in pool:
                chances = pool[rarity]
                weight += chances

                if keyNum <= weight:
                    result.append(rarity)
                    break

        return result        

while True:    
    result = gacha()
    for rarity in result:
        print(rarity)

    replay = input(Fore.CYAN + "Continue? (Y/N): ").upper()

    if replay != "Y":
        print("Gamblers quit before they win big...")
        break