"""
This application splits total bill and calculates tip.
"""

from logo import logo

print(logo)
print("This application calculates tip and splitting bills.\n")


def app_func():

    # Initial User Prompts
    try:
        amount = float(input("How much is your bill?\n"))
    except ValueError:
        print("That's not a number. Try Again!!!\n")
        app_func()
    else:
        bill = format(amount, '.2f')
        print(bill)


app_func()

