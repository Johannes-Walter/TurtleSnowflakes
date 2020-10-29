#!/bin/python3
import turtle
shelly = turtle.Turtle()
for i in range(10):
    for i in range(2):
        shelly.forward(100)
        shelly.right(60)
        shelly.forward(100)
        shelly.right(120)
    shelly.right(36)