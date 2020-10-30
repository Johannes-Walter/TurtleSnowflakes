#!/bin/python3

import turtle
import random

shelly = turtle.Turtle()
turtle.Screen().bgcolor("white")
colors = ["blue", "cyan", "purple", "grey", "pink", "violet", "black"]
shelly.color("cyan")


def branch():
    for i in range(3):
        shelly.color(random.choice(colors))
        for j in range(3):
            shelly.forward(30)
            shelly.backward(30)
            shelly.right(45)
        shelly.left(90)
        shelly.backward(30)
        shelly.left(45)
    shelly.right(90)
    shelly.forward(90)

# testing stuff
for k in range(8):
    branch()
    shelly.left(45)
