from random import *

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+','-','_']

print("wELCOME to the password genertaor!!")

lett_num = int(input("How many letters would you like in your password?\n"))
numb_num = int(input("How many numbers would you like in your password?\n"))
sym_num = int(input("How many symbols would you like in your password?\n"))

final_list = choices(letters,k=lett_num) + choices(numbers,k=numb_num) + choices(symbols,k=sym_num)
print(final_list)
shuffle(final_list)
password = ""
for elem in final_list :
    password += elem

print(f"Your password is : {password}")