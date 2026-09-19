import random as rd
from colorama import init, Fore, Back, Style
init(autoreset=True)

while True:
    while True:
        try:
            min = int(input("Input min: "))
            max = int(input("Input max: "))
            tries = int(input("Input max guess (0 = Inf): "))
        except ValueError:
            print(Fore.RED + "Invalid input!")
            continue
        break

    if tries <= 0:
        tries = float("Inf")

    if max < min:
        print(Fore.RED + "ERROR: Max cannot be lower than min!")
        break

    answer = rd.randint(min, max)

    guessed = False
    trial = 0

    while guessed == False:
        if trial >= tries:
            print(Fore.RED+"You failed to guess the number!")
            print(Fore.CYAN + f"The correct number is {answer}!")
            break

        guess = int(input("Guess the number: "))

        if answer > guess:
            print(f"Number is higher than {guess}!")
        elif answer < guess:
            print(f"Number is lower than {guess}!")
        else:
            print(Fore.GREEN + f"You guessed the correct number! {answer}")
            guessed = True

        trial += 1

    replay = input("Continue? (Y/N): ").upper()
    if replay != "Y":
        print("Thanks for playing!")
        break        

    

