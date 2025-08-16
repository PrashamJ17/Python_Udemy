#  two types of scopes , 
#  a scope can be anything a variable , function , etc.
# 1. Global scope
#  Local scope
#  global scope is defined in the namespace , i.e it is not defined within a functio .
#  it can be accesed from anywhere outside or inside a function

# Local scope is defined outside the namespace , i.e within a function 
# it cannot be accesed outside the function. 
# eg. 

game = 33 # Global Variable(scope)

def func():
    Play = 45 # local variable
    # game = 99 # this is also a local variable with the same name
    
    # i can't do the following :
    global game # this tels that there is a global variale named before the function which needs to be accesed
    # this is how using global we can modify global variables inside a function
    game += 1
    print(game)
    print(Play)
# it is avised to not use the same name of local and global variables . 
#  it is also advised to not modify global scopes inside a functon
func()
print(game)
# print(Play) # this gives error because its not deined in the namespace
# once Play is alsodefind in the namespace it becmes a global variable

#  There is nothing like block scope in python

# Global variables are ost often writen in all caps and with underscores '-'
#  eg: 
PI = 3.1248 # global variables
HELLO = 'world' # global variables


