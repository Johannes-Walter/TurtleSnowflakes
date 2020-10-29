#!/bin/python3

import turtle
import random
shelly = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colors = ["blue", "white", "purple", "cyan"]
shelly.color("cyan")
for i in range(10):
    for j in range(2):
        shelly.forward(100)
        shelly.right(60)
        shelly.forward(100)
        shelly.right(120)
    shelly.right(36)
    shelly.color(random.choice(colors))
