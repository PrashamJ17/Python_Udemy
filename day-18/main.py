from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("orange")

for i in range(4):
    timmy_turtle.forward(100)
    timmy_turtle.left(90)

my_screen = Screen()
my_screen.exitonclick()

