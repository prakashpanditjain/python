from dateutil.relativedelta import relativedelta
from dateutil.utils import today


class Finance:
    def __init__(self):
        # Initialize the class with an amount input from the user
        self.amount = int(input("Enter an amount \n"))

    def calculate_days_and_send_msg(self):
        # Ask if today's date is the start date for financing
        date_given = input(f"Can you tell me, today you have given {self.amount}? (yes/y or no/n) \n")
        if date_given.lower() in ['yes', 'y']:
            # Set the start date to today if the response is 'yes'
            start_date = today()
            print(f"Start date: {start_date}")

            # Get the duration for which the financing is being calculated (e.g., 3 or 6 months)
            months = int(input("This finance is for 3 months or 6 months or multiple of 3 \n"))

            # Calculate interest based on a fixed rate for one lakh (100,000)
            interest_for_lakh = 100000 * 0.03 * months
            interest_for_amount = (self.amount * interest_for_lakh) / 100000
            print("Interest for given amount for given period is: ", interest_for_amount)

            # Calculate the total amount to be financed after deducting the interest
            amount_to_be_financed = self.amount - interest_for_amount
            print("Amount to be financed: ", amount_to_be_financed)

            # Calculate the distribution for the first part (90% of the amount)
            split = [(1 - 0.1) / months] * int((months - (months / 3)))
            sum_of_split = sum(split)  # Sum of the initial split to find the remaining part

            # Calculate the remaining amount to be distributed across the remaining months
            remaining_amount = 1 - sum_of_split
            amount_for_remaining_months = [remaining_amount / (months // 3)] * int(months / 3)

            # Combine both parts to form the full distribution of amounts per month
            full_split = split + amount_for_remaining_months

            # Calculate the monthly break-up of amounts based on the full split, scaled to the actual amount
            monthly_breakup_of_amount = [amount * 100000 for amount in full_split]

            # Adjust the amounts for the user's specific amount
            monthly_breakup_of_amount_other_than_lakh = [
                (amount * self.amount) / 100000 for amount in monthly_breakup_of_amount
            ]
            print(f"Monthly Breakup of amount to be collected: {monthly_breakup_of_amount_other_than_lakh}")

            # Create a list of tuples with formatted month dates and corresponding amounts
            months_amount = [
                ((start_date + relativedelta(months=i)).strftime("%Y-%m-%d"), amount)
                for i, amount in enumerate(monthly_breakup_of_amount_other_than_lakh)
            ]
            print(f"Amount Per Month for given Amount {self.amount}: ", months_amount)


if __name__ == '__main__':
    # Create an instance of the Finance class and call the method to perform the calculations
    finance_instance = Finance()
    finance_instance.calculate_days_and_send_msg()