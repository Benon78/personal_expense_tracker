from config import HEADER_WIDTH
from calculations import (
    calculate_category_totals,
    calculate_total_expenses,
    calculate_balance,
    calculate_total_income,
    get_highest_expense_category
)


# REPORTING AND APPLICATION INTEGRATION
# Format one transaction


def display_transaction(transaction: dict) -> None:
    """
    Format and display one transaction.
    Args:
        transaction (dict): A single transaction dictionary.
    Returns:
        None: Prints the formatted transaction details.
    """
    # unpacking the dictionary
    transaction_id = transaction['id']
    transaction_type = transaction['type'].upper()
    transaction_amount = transaction['amount']
    transaction_date = transaction['date']
    transaction_category = transaction['category'].capitalize()
    transaction_description = transaction['description']

    # Display the transaction neatly
    print(f"""
{'='*HEADER_WIDTH}
{'TRANSACTION DETAILS':^50}
{'='*HEADER_WIDTH}
Transaction ID : {transaction_id}
Date           : {transaction_date}
Type           : {transaction_type}
Category       : {transaction_category}
Description    : {transaction_description}
Amount         : TZS {transaction_amount:,}
{'='*HEADER_WIDTH}
""")

# Format and display all transactions


def display_transactions(transaction_list: list[dict]) -> None:
    """
    Format and display all transactions
    Args:
        transaction_list (list[dict]) : A list of all transactions
    Returns:
        None: Print formatted all transaction details
    """
    print(f"""
{'='*HEADER_WIDTH}
{'ALL TRANSACTIONS':^50}
{'='*HEADER_WIDTH}
""")

    # If there is not transaction display the error message
    if not transaction_list:
        print(
            f'There is not transactions. Please add some transactions and view again!\n\n{'='*HEADER_WIDTH}')
        return

    # print the transaction header
    header = f"{'ID':<4}{'DATE':<11}{'TYPE':<9}{'CATEGORY':<11}{'AMOUNT':>15}\n{'-'*HEADER_WIDTH}"
    print(header)

    # Print all transactions in a format
    for transaction in transaction_list:
        transaction_id = transaction['id']
        transaction_type = transaction['type'].upper()
        transaction_amount = transaction['amount']
        transaction_date = transaction['date']
        transaction_category = transaction['category'].capitalize()
        format_amount = f'{transaction_amount:,}'
        print(f"{transaction_id:<4}{transaction_date:<11}{transaction_type:<9}{transaction_category:<11}{format_amount:>15}")

    total_transactions = len(transaction_list)

    # Print the footer
    print(f"""{'-'*HEADER_WIDTH}
Total transactions: {total_transactions}

{'='*HEADER_WIDTH}
""")

# Format and display all financial summary


def display_financial_summary(transaction_list: list[dict]) -> None:
    """
    Format and display all financial summary
    Args:
        transaction_list (list[dict]) : A list of all transactions
    Returns:
        None: Print formatted all financial details
    """
    print(f"""
{'='*HEADER_WIDTH}
{'FINANCIAL SUMMARY':^50}
{'='*HEADER_WIDTH}
""")

    total_income = calculate_total_income(transaction_list)
    total_expenses = calculate_total_expenses(transaction_list)
    current_balance = calculate_balance(transaction_list)

    print(f"""
{'Total Income':<19}: TZS {total_income:>9,}
{'Total Expenses':<19}: TZS {total_expenses:>9,}
{'-'*HEADER_WIDTH}
{'Current Balance':<19}: TZS {current_balance:>9,}

{'='*HEADER_WIDTH}
""")

# format and display expense analysis


def display_expense_analysis(transaction_list: list[dict]) -> None:
    """
    Format and display all expense analysis
    Args:
        transaction_list (list[dict]) : A list of all transactions
    Returns:
        None: Print formatted expense analysis
    """
    print(f"""
{'='*HEADER_WIDTH}
{'EXPENSE ANALYSIS':^50}
{'='*HEADER_WIDTH}
""")

    total_expenses = calculate_total_expenses(transaction_list)
    total_category_expenses = calculate_category_totals(transaction_list)
    highest_category_expenses = get_highest_expense_category(transaction_list)

    # If there is not transaction display the error message
    if not total_category_expenses or not highest_category_expenses:
        print(
            f'No expenses transactions found.\nPlease record an expense to view expense analysis.\n\n{'='*HEADER_WIDTH}')
        return

    print('EXPENSE BY CATEGORY\n')
    print(f"{'Category':<19}{'Amount (TZS)':>10}\n{'-'*HEADER_WIDTH}")
    for category, amount in total_category_expenses.items():
        print(f"{category.capitalize():<19}{amount:>10,}")

    print(f"""{'-'*HEADER_WIDTH}
{'Total Expenses':<19}{total_expenses:>10,}

HIGHEST EXPENSE CATEGORY
""")
    for category, amount in highest_category_expenses.items():
        print(f"{category.capitalize():<19}{amount:>10,}")

    print(f"\n{'='*HEADER_WIDTH}")
