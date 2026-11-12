from config import(
    INCOME_CATEGORIES,
    EXPENSE_CATEGORIES,
    HEADER_WIDTH
)
from validation import(
    get_valid_category,
    get_description,
    get_positive_amount,
    get_transaction_date
)


# Generate transaction ID
def generate_transaction_id(transaction_list: list[dict]) -> int:
    """
    Generate a unique sequential ID based on existing transactions.

    Args:
        transaction_list (list[dict]): List of existing transaction dictionaries.

    Returns:
        int: 1 if list is empty, otherwise highest existing ID + 1.
    """

    if not transaction_list:
        return 1

    # Find the highest id among all existing transactions and add 1
    highest_id = max(transaction["id"] for transaction in transaction_list)
    return highest_id + 1

# Construct transaction dictionary


def create_transaction(transaction_id: int,
                       transaction_type: str,
                       transaction_amount: int,
                       transaction_category: str,
                       transaction_description: str,
                       transaction_date: str) -> dict:
    """Construct transaction dictionary"""
    transaction = {
        "id": transaction_id,
        "type": transaction_type,
        "amount": transaction_amount,
        "category": transaction_category,
        "description": transaction_description,
        "date": transaction_date
    }

    return transaction


# Transaction creation process


def add_transaction(transaction_list: list[dict], transaction_selected: int) -> None:
    """
    This is the function that create the transaction process. Income and expense share much of the same processing logic:
        - Determine transaction type.
        - Select the appropriate category list
        - Validate the amount.
        - Validate category.
        - Collect description and date.
        - Generate an ID.
        - Create a dictionary.
        - Append it to the transaction list.
    """
    transaction_types = {
        1: 'income',
        2: 'expense'
    }

    transaction_type = transaction_types[transaction_selected]

    # Print the Transaction header
    print(f"""
{'='*HEADER_WIDTH}
{f'ADD {transaction_type.upper()}':^50}
{'='*HEADER_WIDTH}
""")

    # request the transaction amount
    transaction_amount = get_positive_amount()

    # load category
    categories = INCOME_CATEGORIES if transaction_type == 'income' else EXPENSE_CATEGORIES

    print('\nSelect category:')
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")

    # get valid transaction category
    transaction_category = get_valid_category(categories)

    # get transaction description
    transaction_description = get_description()

    # get valid transaction date
    transaction_date = get_transaction_date()

    # get the transaction unique ID
    transaction_id = generate_transaction_id(transaction_list)

    # create the transaction dictionary
    transaction_dictionary = create_transaction(
        transaction_id=transaction_id,
        transaction_type=transaction_type,
        transaction_amount=transaction_amount,
        transaction_category=transaction_category,
        transaction_description=transaction_description,
        transaction_date=transaction_date
    )

    # Append transaction to transaction list
    transaction_list.append(transaction_dictionary)

    print(f"""
{'-'*HEADER_WIDTH}
{transaction_type.capitalize()} recorded successfully!

Transaction ID: {transaction_id}
Amount: TZS {transaction_amount:,}
Category: {transaction_category.capitalize()}

{'='*HEADER_WIDTH}
""")
