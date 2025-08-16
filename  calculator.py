from ascii_art import calcul

def calculator(num1,num2,operation):
    if operation == '+':
        output = num1 + num2
        return output
    elif operation == '-':
        output = num1 - num2
        return output
    elif operation == '/':
        output = num1 / num2
        return output
    elif operation == '*':
        output = num1 * num2
        return output
    else :
        return "Wrong input"

calculation = True
while calculation :
    print(calcul)
    n1 = int(input("Enter the first number;\n"))
    calc = True
    while calc:
        n2 = int(input("Enter the second number\n"))
        print("Enter an operation from the following:")
        op = ['+ : addition','- : subtraction','/ : division','* : multiplication']
        for i in range(0,4):
            print(op[i])
        opn = input()
        result1 = round(calculator(n1,n2,opn),2)
        print(f"{n1} {opn} {n2} = {result1}")

        choice = input(f"Type 'y' to continue calculating with {result1} or type 'n' to start new calculation.\n")
        if choice == 'y':
            n1 = result1
        else :
            print("***********-New Calculation Started-*************")
            calc = False
