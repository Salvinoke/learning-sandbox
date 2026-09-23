import random as rand

width = int(input("Input width: "))
height = int(input("Input height: "))

randomnum = rand.randint(1,height-2)
randompos = rand.randint(-(width//2-1),(width//2-2))

leftspace,rightspace = (width//2-1),(width//2-2)

for i in range(height):
    if i == 0 or i == height-1:
        print("*"*width)
    elif i == randomnum:
        print("*"+" "*(leftspace+randompos) + "|" + " "*(rightspace-randompos) + "*")
    else:
        print("*" + " "*(width-2) + "*")