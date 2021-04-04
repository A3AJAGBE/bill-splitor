"""
This application splits total bill and calculates tip.
The term environment needs to be set for the clear function to work properly.
"""
import os
from logo import logo

print(logo)
print("This application calculates tip and can be used to split bills.")
print("To prevent starting again, type valid inputs only.\n")


# clear function
def clear():
    """This functions clears the console"""
    return os.system('clear')


def split_bill(bill):
    """This function calculates the bill split"""
    try:
        split_by = int(input("How many people are splitting the bill?\n"))
    except ValueError:
        clear()
        print(logo)
        print("Only integers allowed. Try Again!!!\n")
        app_func()
    else:
        if split_by > 1:
            per_person = bill / split_by
            print(f"\nBill to pay is {bill:.2f}\nBill Per Person is {per_person:.2f}")
        else:
            clear()
            print(logo)
            print('Invalid input\n')
            app_func()


def app_func():

    # Initial User Prompts
    try:
        amount = float(input("How much is your bill? "))
    except ValueError:
        clear()
        print(logo)
        print("That's not a number.\n")
        app_func()
    else:
        # Making sure amount is not zero or negative number
        if amount <= 0:
            clear()
            print(logo)
            print('Zero or negative numbers are not allowed.\n')
            app_func()
        else:
            tip_request = input('(Yes or No): Do you want to tip? ').capitalize()

            tip = 0

            # Continue depending on the tip request response
            if tip_request == 'Yes':
                try:
                    tip = int(input("What percentage of tip to add? e.g. 5, 10 or 15 \n"))
                except ValueError:
                    clear()
                    print(logo)
                    print("Only integers allowed. Try Again!!!\n")
                    app_func()
            elif tip_request == 'No':
                tip = tip
            else:
                clear()
                print(logo)
                print('Invalid input.\n')
                app_func()

            # Making sure tip is not negative number
            if tip < 0:
                clear()
                print(logo)
                print('That is a negative number, not allowed.\n')
                app_func()
            else:
                calc_tip = amount * (tip / 100)
                bill = amount + calc_tip
                print(f"\nUpdated Information\nInitial bill of {amount:.2f} with {tip}% = {bill:.2f}")

                split_request = input('(Yes or No): Do you want to split the bill? ').capitalize()

                # Continue depending on the split request response
                if split_request == 'Yes':
                    split_bill(bill)
                elif split_request == 'No':
                    print(f"\nBill to pay is {bill:.2f}")
                else:
                    clear()
                    print(logo)
                    print('Invalid input.\n')
                    app_func()

                print("Thanks for using the application.")


app_func()

