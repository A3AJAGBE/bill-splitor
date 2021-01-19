"""
This application splits total bill and calculates tip.
"""

from logo import logo
print(logo)

print("This application splits bill and can also be used to calculates tip.\n")

TIP = 0

# Inputs
amount = float(input("How much is your bill?\n"))
tip_request = input('Do you want to tip? Yes or No\n').title()

# Continue depending on the tip request response
if tip_request == 'Yes':
    TIP = int(input("How much tip percentage do you want to add? e.g. 5, 10 or 15 \n"))
elif tip_request == 'No':
    TIP = 0
else:
    print('Invalid input')

calc_tip = (amount * (TIP / 100))
bill = amount + calc_tip

# splitting the bill by how many people?
split_bill_num = int(input("How many people are splitting the bill?\n"))

if split_bill_num > 1:
    bill_per_person = bill / split_bill_num
    print(f"Your new total: {bill:.2f}\nTip: {calc_tip:.2f}\nBill Per Person: {bill_per_person:.2f}\n")
elif split_bill_num == 1:
    print(f"Your new total is: {bill:.2f}\nTip: {calc_tip:.2f}\n ")
else:
    print('Invalid input')

print("Thanks for using the application\n")

