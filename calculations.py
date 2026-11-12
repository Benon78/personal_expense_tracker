# IMPLEMENTING FINANCIAL FUNCTIONS

# Sum income transactions

def calculate_total_income(transaction_list: list[dict]) -> int:
    """Sum income transactions"""
    total_income = sum(transaction['amount']
                       for transaction in transaction_list if transaction['type'] == 'income')
    return total_income

# Sum expense transactions


def calculate_total_expenses(transaction_list: list[dict]) -> int:
    """Sum expense transactions"""
    total_expense = sum(transaction['amount']
                        for transaction in transaction_list if transaction['type'] == 'expense')
    return total_expense

# calculate the remain transaction balance


def calculate_balance(transaction_list: list[dict]) -> int:
    """
    Calculate the remain transaction balance
    Args:
        transaction_list(list[dict]): A list of all transactions
    Returns:
        int: Current balance (Total balance - Total expenses)
    """
    current_balance = calculate_total_income(
        transaction_list) - calculate_total_expenses(transaction_list)
    return current_balance

# Sum expenses by category


def calculate_category_totals(transaction_list: list[dict]) -> dict[str, int]:
    """
    Calculate the total amount spent by expense category.
    Args:
        transaction_list (list[dict]): A list of all transactions.
    Returns:
        dict[str,int]: Total expenses grouped by category.
    """
    total_category_expense: dict[str, int] = {}

    for transaction in transaction_list:
        # Process expense only
        if transaction['type'] == 'expense':
            category = transaction["category"]
            amount = transaction["amount"]

            # Add to existing category or initialize a new one
            if category in total_category_expense:
                total_category_expense[category] += amount
            else:
                total_category_expense[category] = amount
    return total_category_expense

# Identify the largest category


def get_highest_expense_category(transaction_list: list[dict]) -> dict[str, int]:
    """Identify the largest expense categories"""
    total_category_expense = calculate_category_totals(transaction_list)
    if not total_category_expense:
        return {}

    max_amount = max(total_category_expense.values())

    # Filter for all items that match that exact amount
    highest_expenses = {category: amount
                        for category, amount in total_category_expense.items()
                        if amount == max_amount
                        }
    return highest_expenses
