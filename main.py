"""
This application splits total bill and calculates tip.
"""

from logo import logo

print(logo)
print("This application calculates tip and splitting bills.\n")


def app_func():

    # Initial User Prompts
    try:
        amount = float(input("How much is your bill? "))
    except ValueError:
        print("That's not a number. Try Again!!!\n")
        app_func()
    else:
        # bill = format(amount, '.2f')

        tip_request = input('(Yes or No): Do you want to tip? ').capitalize()

        # Continue depending on the tip request response
        if tip_request == 'Yes':
            try:
                TIP = int(input("What percentage of tip to add? e.g. 5, 10 or 15 \n"))
            except ValueError:
                print("That's not a number. Try Again!!!\n")
                app_func()
        elif tip_request == 'No':
            TIP = 0
        else:
            print('Invalid input\n')
            app_func()

        # Complete the first calculation
        calc_tip = amount * (TIP / 100)
        bill = amount + calc_tip
        print(f"Initial bill of {amount} with {TIP}% = {bill:.2f}")


app_func()

