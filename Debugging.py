# age = int(input("Enter your age\n"))

# now a person may type in letters and not i numerical form . 
#  this may generate a VALUE ERROR. 
# Hence after debugging when we know whuch errir is showing we can use :
# TRY AND EXCEPT CODES . 

try :
    age = int(input("Enter your Age:\n"))
except ValueError :
    print("Enter in Numerical form")
    age = int(input("Enter your Age:\n"))

if age > 18 :
    print(f"You can drive a car {age}.")


# If you have a different output than expected then 
# always print each output . using ther print function
# At each step so may know where the actual problem lies .

# You can also use a debugger like thonny for bigger projects . 
# you should use the debugger of the code edditor you are using 
#  in my case vs code or proper debugging