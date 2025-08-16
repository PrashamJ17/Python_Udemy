print("Welcome to thr tip calculator !")
bill = int(input("What is the total bill amount? ₹"))
Tip = int(input("How much tip would you like to give ?10, 12 or 15 ?"))
people = int(input("How many people to split the bill? "))
per_person = (bill + (Tip * bill)/100)/people
print("Each person shouldpay : ₹" +  str(per_person))
print("Hello World")
