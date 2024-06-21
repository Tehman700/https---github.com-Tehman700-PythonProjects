from turtle import Turtle,Screen
import random


tehman = Turtle()
tehman.shape("turtle")
tehman.color("Magenta")


forwar = 0
value = 3

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tehman.color(R, G, B)


while True:

    change_color()
    tehman.speed(0)
    for _ in range(value):
        

        tehman.forward(100)
        tehman.right(360/value)
        
    
    value+=1

    if value == 9:
        break

    # for _ in range(4):
    #     tehman.forward(100)
    #     tehman.right(90)
    # for _ in range(5):
    #     tehman.forward(100)
    #     tehman.right(72)
    # for _ in range(6):
    #     tehman.forward(100)
    #     tehman.right(60)
    # for _ in range(7):
    #     tehman.forward(100)
    #     tehman.right(51.428)
    # for _ in range(8):
    #     tehman.forward(100)
    #     tehman.right(45)
    # for _ in range(9):
    #     tehman.forward(100)
    #     tehman.right(40)








scr = Screen()
scr.exitonclick()
