import turtle as t
import time
screen = t.Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0,0.1)
# snake = t.Turtle(shape = "square")

# creating the reactangle shape using the register_shape commnd of turtle screen :
# i can't use the rectangle beacuse in the snaake game the blocks get added as the snake eats , 
# hence for proper working use the below command 

# rect_coord = ((10,30), (-10,30), (-10,-30), (10,-30))
# screen.register_shape("rectangle",rect_coord)
# snake.shape("rectangle")
# snake.color("white")

# another way to create the shape we want is by creating 3 squares
# and placing them one beside another as follows : 

positions = [(0,0),(-20,0),(-40,0)]
snake_blocks = []
for position in positions :
    snake = t.Turtle(shape="square")
    snake.color("white")
    snake.up()
    snake.goto(position)
    snake_blocks.append(snake)


game = True
while game :
    screen.update() # refreshes the screen
    time.sleep(0.1)
    
    for i in range(len(snake_blocks)-1,0,-1): # this starts the loop from last to second (in this it will give us 1 but not 0)and excludes the stop value given
        x_coord = snake_blocks[i-1].xcor()
        y_coord = snake_blocks[i-1].ycor()
        snake_blocks[i].goto(x_coord,y_coord)
    snake_blocks[0].left(90)
    snake_blocks[0].forward(20)
screen.exitonclick()


