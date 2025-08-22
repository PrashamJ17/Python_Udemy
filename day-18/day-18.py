import turtle as t
import random
timmy_turtle = t.Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("orange")



# for i in range(4):
#     timmy_turtle.forward(100)
#     timmy_turtle.left(90)


# chalenge 2 : polygons from triangle to decagon
# for i in range(10):
#     timmy_turtle.forward(10)
#     timmy_turtle.up()
#     timmy_turtle.forward(10)
#     timmy_turtle.down()

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return timmy_turtle.color((r,g,b))

#  challeng-3
# for i in range(3,11):
#     for j in range(i):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(360/i)
#     timmy_turtle.color(random.choice(colours))


# challenge -4 - random walk
# angle = [0,90,180,270]
# timmy_turtle.width(7)
# timmy_turtle.speed("fastest")
# for i in range(200):
#     random_color()
#     timmy_turtle.forward(30)
#     timmy_turtle.setheading(random.choice(angle))

# challenge-5 - spirograph
angle = int(input("Enter the shift angle in integer format: "))
timmy_turtle.speed("fastest")
for circles in range(int(360/angle)):
    random_color()
    timmy_turtle.circle(100)
    timmy_turtle.right(angle)    
    
my_screen = t.Screen()
my_screen.exitonclick()

