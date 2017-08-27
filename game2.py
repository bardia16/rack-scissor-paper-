import random
y = None
x = None
pointx = 0
pointy = 0
game = ["rock", "scissor", "paper"]
def mosavi():
    print("no one win this round try agin :D")
def ywin():
    global pointy
    print("you win this round and you get 1 point")
    pointy += 1
    print("your points: " + str(pointy))
    print("computer points: " + str(pointx))
def xwin():
    global pointx
    print("you lose this round :( computer gets 1 point")
    pointx += 1
    print("your points: " + str(pointy))
    print("computer points: " + str(pointx))
while pointy<3 and pointx<3:
    x = (random.choice(game))
    y = input("Please select your item[rock , scissor, paper]")
    y = str(y)
    if str(y) == game[0] and x == game[-1]:
        xwin()
    elif str(y)== game[-1] and x == game[0]:
        ywin()
    elif y == game[0] and x == game[1]:
        ywin()
    elif y == game[1] and x == game[0]:
        xwin()
    elif y == game[1] and x == game[-1]:
        ywin()
    elif y == game[-1] and x == game[1]:
        xwin()
    elif y == game[0] and x == game[0]:
        mosavi()
    elif y == game[1] and x == game[1]:
        mosavi()
    elif y == game[-1] and x==game[-1]:
        mosavi()
    else:
    	print("Please choose 1 item from this list [rock, scissor, paper]")
if pointx<pointy:
    print("You win!")
    input("Press Enter To Exit")
    quit()
else:
    print("Computer wins!")  
    input("Press Enter To Exit")
    quit()
    