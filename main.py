from config import HEADER_WIDTH
from validation import get_menu_choice
from transactions import add_transaction
from reports import (
    display_expense_analysis,
    display_financial_summary,
    display_transactions
)


# MAIN APPLICATION FUNCTION
def main() -> None:
    """
    Control the entire application
     - Initialize the transaction list
     - Display the menu
     - Receive user selection
     - Call the appropriate function
     - Repeat until the user exits
    """

    # Store all the transactions
    transaction_list: list[dict] = []

    # Print the header of the application
    print(f"""
{'='*HEADER_WIDTH}
{'PERSONAL EXPENSE TRACKER':^50}
{'Currency: TZS':^50}
{'='*HEADER_WIDTH}
""")

    try:
        while True:
            choice = get_menu_choice()
            if choice in (1, 2):
                add_transaction(transaction_list, choice)
            elif choice == 3:
                display_transactions(transaction_list)
            elif choice == 4:
                display_financial_summary(transaction_list)
            elif choice == 5:
                display_expense_analysis(transaction_list)
            elif choice == 6:
                print('\nGoodbye, see you again!\n')
                break
    except KeyboardInterrupt:
        print('\nPersonal expense tracker interrupted by the user.\n')


if __name__ == "__main__":
    main()
