# how do we minus the resources used to make the drink fro the original resources 
# when a drink is ordered , the coins are asked , how do we add those money and check if it is :
#  1. sufficient , 2. less , 3. extra 
# if the money is extra then we need to pay the balance back . how do we get the balance . 
# if the resources to make the drink aren't sufficient then how do we know that ?

from coffee_menu import *

def money(ac_cost,a_money):
    print("Please insert the coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    Total_input = round((quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01),2)

    if Total_input == ac_cost :
        a_money += ac_cost
        return print(f"Here is your {choice} ☕, Enjoy!")
    elif Total_input > ac_cost :
        change = round((Total_input - ac_cost),2)
        print(f"Here is ${change} in change.")
        a_money += ac_cost
        return print(f"Here is your {choice} ☕, Enjoy!")
    else :
        return print("Sorry that's not enough money. Money refunded.")
    
add_money = 0
choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

def c_machine():
    if choice == 'off':
        return print("Turned Off !")
    elif choice == 'report':
        return 
    elif choice == 'espresso' or 'latte' or 'cappuccino' :
        Price = MENU[choice]['cost']
        money(Price,add_money)

            











c_machine()






