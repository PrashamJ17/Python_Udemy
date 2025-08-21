class User: # class is created , naming of class is done as PascalCase - > first letter of every word is capital . 
    # pass # it just passes to the next line of code . {used to remove the errors if there is nothing to be coded for the moment}
    
    def __init__(self,user_id,username): # self is the object that is created . Everything that is written next to self is ate attribute parameter .
        #  we have passed an attribute parameter so that everytime we create an obj using the class we have to pass these attr values as well and not write it separately using "."
        self.user_id = user_id    # we have called the attribute as obj.att and set its value to the parameter passed when the obj is created
        self.username = username  # it is common to use the same name of attribute and the parameter 
        self.followers = 0 # in this attribute we have set the default value to 0 . and not written as a parameter . 
        # for eg . in the insta handle the followeers of a profile start from 0 and increase by 1 hence it is foolish to pass/change the value of attribute everytime someone follows . 
        self.following = 0
    
    # while defining a method in the class we have to laways pqs the self parameter for the object and other parametrs same as the function we did before .
    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_1 = User() # an object is created using the class User
#  to add attributes we use the '.
# after defininng the constructor Now when we try to create to an obj using the above syntax it will give us an error as we have not passed the parameter we defined in the init function of the class . 

user_1 = User("001","Prasham") # this is how we wil create an objcet everytime and pass the values of its attributes . 
# user_1.user_id = "002" # we can still change the value of attribute . 
user_2 = User("002","Pratham")
user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)
print(user_1.user_id)
print(user_1.followers)


# if there are too many objects and thi=eir attributes , we have to create constructors . 
# constructors -> speacial function defined as def __init__(self) within a class
# in the init function we initialize that is create a starting value for our attributes of the obejects

# everytime when a new obj is created using the same class , the init function is triggered . 
