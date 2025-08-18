# how do we minus the resources used to make the drink fro the original resources 
# when a drink is ordered , the coins are asked , how do we add those money and check if it is :
#  1. sufficient , 2. less , 3. extra 
# if the money is extra then we need to pay the balance back . how do we get the balance . 
# if the resources to make the drink aren't sufficient then how do we know that ?

from coffee_menu import *
ad_money = 0

def resources_left(drink,a_money):
    resources['water'] = resources['water'] - MENU[drink]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[drink]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[drink]['ingredients']['coffee']
    resources['Money'] = f"${a_money}"

def money(custom_drink):
    global ad_money
    print("Please insert the coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    Total_input = round((quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01),2)

    if Total_input == MENU[custom_drink]['cost'] :
        ad_money += MENU[custom_drink]['cost'] # to be added to the total profit in the report 
        resources_left(custom_drink,ad_money)
        print(f"Here is your {custom_drink} ☕, Enjoy!")

    elif Total_input > MENU[custom_drink]['cost'] :
        change = round((Total_input - MENU[custom_drink]['cost']),2)
        print(f"Here is ${change} in change.")
        ad_money += MENU[custom_drink]['cost'] # this is also to be added to the profit in the report
        resources_left(custom_drink,ad_money)
        print(f"Here is your {custom_drink} ☕, Enjoy!")

    else :
        print("Sorry that's not enough money. Money refunded.")


def c_machine():
    COOFFEE = True
    while COOFFEE :
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == 'off':    
            return print("Turned Off !")
        
        elif choice == 'report':    
            print(resources)
        
        elif choice == 'espresso' or 'latte' or 'cappuccino' :

            # This below code is to check the resources
            if resources['water'] < MENU[choice]['ingredients']['water']:
                return print("Sorry there is not enough water!")
            if resources['milk'] < MENU[choice]['ingredients']['milk']:
                return print("Sorry there is not enough milk!")
            if resources['coffee'] < MENU[choice]['ingredients']['coffee']:
                return print("Sorry there is not enough coffee!")
            
            # the below code is for the money
            money(choice)
            
c_machine()