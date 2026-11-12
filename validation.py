from datetime import datetime, date
from config import HEADER_WIDTH

# IMPLEMENT MENU, TRANSACTION INPUT AND VALIDATION FUNCTIONS

# display menu
def display_menu() -> None:
    """Display available operational menu"""
    print(f"""
MAIN MENU
\t1. Add Income
\t2. Add Expense
\t3. View Transactions
\t4. Financial Summary
\t5. Expenses Analysis
\t6. Exit

{'-'*HEADER_WIDTH}
""")

# Get user selection


def get_menu_choice() -> int:
    """
    Display the menu and get a valid menu selection
    Returns:
        int: A valid menu choice between 1 and 6
    """
    while True:
        display_menu()
        selection = input('Select an option: ')
        try:
            input_selection = int(selection)
            if 1 <= input_selection <= 6:
                return input_selection
            print('Invalid option. Please select a number between 1 and 6.')
        except ValueError:
            print('Invalid input. Please enter a whole number.')

# Validate the transaction amount
def get_positive_amount() -> int:
    """Get and validate the transaction amount from the user
    Returns:
        int : A valid positive transaction amount
    """
    while True:
        input_amount = input('Enter amount: ')
        try:
            amount = int(input_amount.replace(',', '').strip())
            if amount > 0:
                return amount
            print('Invalid amount. Please enter a number greater than zero.\n')
        except ValueError:
            print('Invalid input. Please enter a whole number without decimals.\n')

# Validate selected category
def get_valid_category(category_list: list[str]) -> str:
    """
    Validate the category for the transaction
    Args:
        category_list (list): Transaction category list
    Returns:
        category (str): A valid transaction category 
    """
    while True:
        selected_option = input('\nSelect category option: ')
        try:
            category_selected = int(selected_option.strip())
            if 1 <= category_selected <= len(category_list):
                return category_list[category_selected - 1]

            print(
                f'Invalid category. Please enter a number between 1 and {len(category_list)}.\n')

        except ValueError:
            print('Invalid option. Please enter a whole number.\n')

# Collect transaction description
def get_description() -> str:
    """This function request the transaction description"""
    while True:
        description = input('\nEnter description: ').strip()
        if len(description) >= 5:
            return description
        print('The transaction description should have at least 5 characters.\n')


# Collect and validate date
def get_transaction_date() -> str:
    """
    Collect and validate a transaction date.
    """

    while True:
        typed_date = input(
            f"\nPress Enter to use today's date.\nEnter a date (YYYY-MM-DD): ").strip()

        # Use today's date when the user presses Enter.
        if not typed_date:
            return date.today().isoformat()

        try:
            # check if the input matches the format (YYY-MM-DD)
            parsed_date = datetime.strptime(typed_date, "%Y-%m-%d").date()
            return parsed_date.isoformat()
        except ValueError:
            print(
                'Invalid date format. Please enter a valid date in YYYY-MM-DD format.\n')
