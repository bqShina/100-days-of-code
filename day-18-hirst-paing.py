# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# color_list = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     color_list.append((r, g, b))
# print(color_list)
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setposition(-100, -100)
color_list = [(246, 241, 244), (222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149), (221, 73, 90),
              (243, 208, 99), (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70),
              (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75),
              (213, 222, 213), (1, 98, 119), (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228),
              (24, 98, 61)]


def draw_row():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


for n in range(10):
    draw_row()
    tim.setposition(-100, -100 + 50 * (n + 1))


screen = t.Screen()
screen.exitonclick()
