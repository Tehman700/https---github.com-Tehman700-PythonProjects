from turtle import *
import time
scr = Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.tracer(0)


starting_snake = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_snake:
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(position)
    segments.append(snake)


game_on = True

while game_on:
    scr.update()
    time.sleep(.11)

    for seg in segments:
        seg.forward(20)




scr.exitonclick()