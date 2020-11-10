
"""
This application calculates tip and assist in spliting bills.
"""

print("Welcome to A3AJAGBE TipCalc\n")

amount = float(input("What is your bill total?\n"))

tip = int(input("How much tip percentage do you want to add? e.g. 5, 10 or 15 \n"))

calc_tip = (amount * (tip / 100))

total_share = int(input("How many people will be sharing the bill?\n"))

bill = amount + calc_tip
bill_split = bill / total_share

print(f"Your new total is: {bill:.2f}, and the split per person is: {bill_split:.2f}\n")

print("Thanks for using the application!!!\n")


