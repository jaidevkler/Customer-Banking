# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
# Import sys 
import sys

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
   
    try:
        # Prompt the user to set the savings balance, interest rate, and months for the savings account.
        savings_balance = float(input("Enter savings balance: "))
        savings_interest = float(input("Enter savings interest rate: "))
        savings_maturity = int(input("Enter savings mauturity in months: "))
        # Check if the values are greater than zero
        if savings_balance < 0 or savings_interest < 0 or savings_maturity < 0:
            sys.exit('Entered values cannot be negative')
    except ValueError:
        # Exit in case if a wrong data type is entered
        sys.exit('Entered value are of an incorrect data type!')

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The interest earned is ${interest_earned:,.2f} and the updated savings balance is ${updated_savings_balance:,.2f}")

    try:
        # Prompt the user to set the CD balance, interest rate, and months for the CD account.
        cd_balance = float(input("Enter CD balance: "))
        cd_interest = float(input("Enter CD interest rate: "))
        cd_maturity = int(input("Enter CD maturity in months: "))
        # Check if the values are greater than zero
        if cd_balance < 0 or cd_interest < 0 or cd_maturity < 0:
            sys.exit('Entered values cannot be negative')
    except ValueError:
        # Exit in case if a wrong data type is entered
        sys.exit('Entered value are of an incorrect data type!')

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The interest earned is ${interest_earned:,.2f} and the updated CD account balance is ${updated_cd_balance:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()