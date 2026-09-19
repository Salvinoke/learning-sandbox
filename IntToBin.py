from colorama import init,Fore
import math
init(autoreset=True)

def convert():
    while True:
        try:
            num = int(input("Input number to convert: "))
        except ValueError:
            print(Fore.RED + "Num value must be integer!")
            continue
        break

    binary = ""

    if num == 0:
        return "0"
    
    lastnum = abs(num)

    while lastnum >= 1:
        binary += str(lastnum%2)
        lastnum = lastnum // 2

    binary = binary[::-1]
    if num < 0:
        binary = "b" + binary

    return binary
    
binary = convert()
print(Fore.GREEN + binary)

    