import turtle as t
POSITIION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake :
    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    #  step -1 : Building the body of the snake 
    def create_snake(self):

        for i in range(len(POSITIION)):
            self.segment = t.Turtle(shape="square")
            self.segment.color("white")
            self.segment.penup()
            self.segment.goto(POSITIION[i])
    
            self.snake_blocks.append(self.segment)
    #  step -1 - completed  : Building the body of the snake 

    #  step-2 : moving the snake - in this we tell the blocks to take up the position of the block ahead . 
    # and so on we start from the last till the srecond block . so when the first block moves every block behind it folows .
    def move(self):
        for i in range(len(self.snake_blocks)-1,0,-1):
            X_pos = self.snake_blocks[i-1].xcor()
            Y_pos = self.snake_blocks[i-1].ycor()
            self.snake_blocks[i].goto(X_pos,Y_pos)
        self.head.forward(MOVE_DISTANCE)
    #  step-2 Completed : moving the snake

    #  Step-3 : Controlling the snake :
    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
    

    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)