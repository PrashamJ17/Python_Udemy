# procedural prof=gramming --> that we have beeen doing for these days . 
# it is basicaaly writting the codes in a sequencial format , creating functions , where one functins is connected to others and so on 
# it gets very clumsy and crowded and the logic get clouded while writing big codes in this format . 

# this is where OOPS come in handy . 
# object oriented programming

# attributes - also be a variable - associated with a model object 
# methods - basically functions - that specific object does . 

#  in object oriented programming we try to model real world objects and 
# these objects have attributes(variables that define them) and methods(functions that they do)

# we can have multiple objects / versions of the same objects . 
# so basically if we were to model waiter for a restraunt, then we can have multiple waiters having same att and functionality . 
# Thus here WAITER becomes a class(blueprint used to create actual objects) and the multiple model becomes the OBJECT

# we will start in oops with the turtle graphics library and importing its classes and objects and their methods to get familiar with oops programming . 

from turtle import *     # this imports everything in the turtle library and we can use them without writing the prefix turtle everytime
# if typing “turtle” over and over again becomes tedious, use for example import turtle as t instead - t.width() , etc 
# the first import is mostly avoided if we are importing to many modules as its a risk of name conflict . 
# hence the option of "import turte as t" is preferred 

timmy = Turtle() # this creates an object called timmy from the clss turtle . 
#  timmy -> object , Turtle() -> class
# print(timmy)

# timmy.shape("turtle")  # we are calling a method to change the shape of timmy and changing ti turtle (its a built in shape) , 
# to know more see the docs of turtle on python . 
# remember we have to call all these functions before the screen class / object to make it appear on the screen

# timmy.forward(70) # you will see that the turtle has moved fwd in the dirn it was facing by 70px
# timmy.right(90) # this turns (rotates) the turtle to the right by 90deg angle . 
# timmy.left(180) # same turns/rotates turtle to left by 180 deg
# timmy.color("blue")  # changes the color of turtle to blue . 
# to change the color there are too may things that you can type in and a list of a lot of colors . 
# see the documentation 

# to form a triangle : 
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)

# timmy.width(3) # to change the width of the line its following
# timmy.forward(100)

# timmy.up() # this lifts the pen up --> thus it doen=snt draw a line as it moved and directly jumps
# timmy.forward(100)

# timmy.down() # to bring the pen down again to draw

# timmy.home() # this draws the turtle back at default position - 0,0
# useful when the turtle is off-screen 

# print(timmy.pos()) # this gives the position/coorditnates of the turtle in the terminal window and not on the screen .

# thr following code prints a pattern on the screen 
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)


# the folllowing code creates a star and after that a circle with border of red and inside fill of yellow
# timmy.color("red")
# timmy.fillcolor("yellow")
# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1: # this tells us if the turtle is back at the home position , if it is then we stop , break .
#         break
# timmy.circle(30)
# timmy.end_fill()


# Now to show the object on the screen , with the graphics interface 
#  we will use the screen class from the turtle lib . 
# with the screen class will create an object that which represents a screen in which the "timmy" will be shown

# my_screen = Screen()
# print(my_screen.canvheight) # for the attributes of an object it is written as "object_name.attribute"
# canvheight is a built in attribute of turte / class screen which gives the screen interface a height of 300px

# to call the function / method of the object , we have to call it the same way as attribute . 
# "object_name.func()"

# my_screen.clearscreen() # this is to clear the screen 

# my_screen.exitonclick() # the exitonclic function --> closes the interface window only when clicked on the screen 
# the code only exits when the interface is clicked on . 

# now on the screen preview we can see that our turtle - > timy is shown as a cursor/arrow . 
#  we can also change he shape of timmy . 

