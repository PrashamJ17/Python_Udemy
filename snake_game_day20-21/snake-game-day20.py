# Steps to build the Snake Game. :

#  step -1 : Building the body of the snake 
#  step-2 : moving the snake
#  step-3 : Moving the snake 
#  step-4 : Detect collision with the food to increase the length of the snake
#  step-5 : Creating the scorebard
#  step-6 : Game ending conditions - 
#          1. Coliision with the side walls 
#          2. Collision with itself 
import turtle as t
import time    # to lower the time of animation so that the bocks move slowly 
from snake import Snake
#  Screen Set-up
screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # this turns the screen off and until the update command is not called the screen doesn't show anything.
#  the tracer command turns off the animation and stops the screen 
# thus the blocks don't move separately and instead when ther update command is called the blocks move together . 


#  step -1 : Building the body of the snake 
snake = Snake()
#  step -1 - completed  : Building the body of the snake 


# Step-3 : Controlling the Snake using arrow keys 
screen.listen()
screen.onkey(key = "Up",fun=snake.up)
screen.onkey(key = "Down",fun=snake.down)
screen.onkey(key = "Right",fun=snake.right)
screen.onkey(key = "Left",fun=snake.left)
# Step-3- Completed : Controlling the Snake using arrow keys 

#  step-2 : moving the snake - in this we tell the blocks to take up the position of the block ahead . 
# and so on we start from the last till the srecond block . so when the first block moves every block behind it folows .
game_is_on = True
while game_is_on :
    screen.update() # this refreshes the screen and allows the screen to show the animation , the blocks move together .
    time.sleep(0.1) # this puts some delay so that the blocks move together . 
    
    snake.move()
#  step-2 Completed : moving the snake


screen.exitonclick()