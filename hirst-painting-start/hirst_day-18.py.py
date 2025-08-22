# import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('/Users/prasham/Desktop/Python udemy/hirst-painting-start/Hirst_img.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

# print(rgb_colors)
t.colormode(255)
color_list = [(245, 243, 238),(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
tim.color("light blue")
y = 0
for i in range(10):
    for j in range(10):
        
        tim.dot(20,random.choice(color_list))
        tim.up()
        tim.fd(30)
        tim.down()
    y += 30
    tim.teleport(0,y)
tim.up()
tim.home()


my_screen = t.Screen()
my_screen.exitonclick()