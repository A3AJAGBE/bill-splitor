"""
This application splits total bill.
"""

from logo import logo
print(logo)

print("This application splits bill and can also be used to calculate tips.\n")

TIP = 0

# Inputs
amount = float(input("How much is your bill?\n"))
tip_request = input('Do you want to tip? Yes or No\n').title()

# Continue depending on the tip request response
if tip_request == 'Yes':
    TIP = int(input("How much tip percentage do you want to add? e.g. 5, 10 or 15 \n"))
elif tip_request == 'No':
    print('No tip')
else:
    print('Invalid input')

calc_tip = (amount * (TIP / 100))
print(f"{calc_tip:.2f}")
bill = amount + calc_tip

print(bill)

