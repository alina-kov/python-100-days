"""
Hirst-style dot painting using Turtle graphics.
Colors were extracted from an image using colorgram.
Project from Angela Yu's 100 Days of Code (Day 18).
"""

# import colorgram
from turtle import Turtle, Screen
import random

# Extract colors from the image using colorgram
# (used only once to build a fixed color palette)
# colors = colorgram.extract("image.jpg", 20)
# list_of_colors = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors]
# print(list_of_colors)

# Turtle screen setup
screen = Screen()
screen.colormode(255)

# Color palette extracted from the image
color_list = [
    (232, 241, 239), (1, 10, 30), (229, 235, 242), (239, 232, 238), 
    (122, 95, 41), (71, 31, 21), (219, 225, 242), (238, 212, 72), 
    (220, 81, 59), (226, 117, 100), (239, 125, 122), (93, 1, 21),
    (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72),
    (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29)
]

# Initial turtle setup
timmy = Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")

# Set starting position
start_x = -300
start_y = -300
timmy.goto(start_x, start_y)


# Draw one horizontal row of dots
def make_dot():
    for _ in range(13):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)


# Draw the hole picture
for _ in range(13):
    make_dot()
    start_y += 50
    timmy.goto(start_x, start_y)


screen.exitonclick()
