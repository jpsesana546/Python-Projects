"""
Tip Calculator 0_0

Problem:
    If the bill was $150.00, split between 5 people, with 12% tip. 
    Each person should pay (150.00 / 5) * 1.12 = 33.6
    Format the result to 2 decimal places = 33.60
"""

#Enter beginning messsage
print("Welcome to the Tip Calculator!")

#Input total bill
bill = float(input("What is your total bill?\n$"))

#How many people will be sharing the bill
n_of_people = int(input("How many people will share the bill?\n"))

#Input desired tip
tip_amount = int(input("What is your desired tip?\nTip: 10,12,or 15 percent\n"))

#Add tip to total
bill_with_tip = bill * (tip_amount / 100 + 1)

#Divide by number of people
bill_per_person = round(bill_with_tip / n_of_people, ndigits=2)
bill_per_person = "{:.2f}".format(bill_per_person)

#Print price per person
print(f"The total per person comes to: ${bill_per_person}\n")