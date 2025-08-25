import turtle as t
import random

#  etch - a - sketch

# tim = t.Turtle()
# def move_forward():
#     tim.forward(20)
# def move_back():
#     tim.backward(20)
# def move_left():
#     tim.left(15)
# def move_right():
#     tim.right(15)
# screen = t.Screen()

# screen.listen() # this tells the creen to do some function provided when a key is pressed as specified.
# screen.onkey(key = "w",fun = move_forward)
# screen.onkey(key="s",fun = move_back)
# screen.onkey(key="a",fun = move_left)
# screen.onkey(key="d",fun = move_right)
# screen.onkey(key="c",fun = screen.resetscreen)

# screen.exitonclick()


# higher order functions are basically functions within a function . 
# that is a functions reurns another funtion as a result . 

screen = t.Screen()
screen.setup(width = 700,height = 600) # to set up the screen size/canvas size .

colors = ["red","green","blue","yellow","orange","purple"]
y_position = [125,75,25,-25,-75,-125]
all_turtles = []
for turt in range(0,6):
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.color(colors[turt])
    new_turtle.penup()
    new_turtle.goto(x = -330,y = y_position[turt] )
    all_turtles.append(new_turtle)
    
user_bets = screen.textinput(title = "Place Your Bets!",prompt = "Which turtle will win the race")
print(user_bets)
if user_bets :
    race_is_on = True
while race_is_on :
    for turtle in all_turtles:
        if turtle.xcor() > 330 :
            win_color = turtle.pencolor()
            race_is_on = False
        rand_dist = random.randint(0,10)
        turtle.fd(rand_dist)
        
if win_color == user_bets :
    print("You've won'")
else :
    print(f"You've lost . The {win_color} turtle won the race !")





screen.exitonclick()
