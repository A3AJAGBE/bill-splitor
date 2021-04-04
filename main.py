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
        # Making sure amount is not zero or negative number
        if amount <= 0:
            print('That input is not allowed.\n')
            app_func()
        else:
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

            # Making sure tip is not negative number
            if TIP < 0:
                print('That is a negative number, not allowed.\n')
                app_func()
            else:
                # Complete the first calculation
                calc_tip = amount * (TIP / 100)
                bill = amount + calc_tip
                print(f"Initial bill of {amount:.2f} with {TIP}% = {bill:.2f}")


app_func()

