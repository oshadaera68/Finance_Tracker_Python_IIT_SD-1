# import the json module
import json

# import the datetime module
from datetime import datetime

# Global List
transactions = []


# load all transactions
def load_transactions():
    try:
        with open("Data.json", "r") as f:
            trans_data = json.load(f)  # load all transactions in the file

    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or contains invalid JSON data,
        # initialize transactions as an empty list
        trans_data = []

    for x in trans_data:
        print(x)


# Save the transactions
def save_transactions():
    # write the data in the json file
    with open("Data.json", "w") as f:
        json.dump(transactions, f, default=str, indent=2)  # getting the string for default and indentation in 2.


# Validations

# Date Validation
def is_valid_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')  # formatting the date
        return True
    except ValueError:
        return False


# add the transactions (main function)
def add_transaction():
    while True:
        print("-----------------------------------------")
        print("|\t\t\t Add Transaction \t\t\t|")
        print("-----------------------------------------")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Back to main menu")
        choice = input("Enter the choice: ")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
    main_menu()


# Add The Income.
def add_income():
    print("-----------------------------------------")
    print("|\t\t\t Add Income \t\t\t\t|")
    print("-----------------------------------------")
    while True:
        amount = int(input("Enter an Amount: "))
        if not 4 <= amount <= 8:
            category = input("Enter a Category: ")
            if category == '':
                print("Invalid Input. Please enter a category.")
                continue

            type_input = input("Enter the type: ")
            if type_input.lower() != "income":
                print("Please type 'Income' for income.")
                continue

            date = input("Enter the date: ")
            if not is_valid_date(date):
                print("Please type the date correctly.")
                continue

            transaction = [amount, category, type_input, date]
            transactions.append(transaction)
            save_transactions()

            choice_set = input("Transaction added successfully! Do you want to add a New Transaction? [Y/N]: ")
            if choice_set.lower() == 'y':
                continue
            elif choice_set.lower() == 'n':
                break
            else:
                print("Invalid Entry!! Please try again!")

    # After breaking out of the loop (when choice_set is 'n'), return to the main menu
    main_menu()


def add_expense():
    print("-----------------------------------------")
    print("|\t\t\t Add Expense \t\t\t\t|")
    print("-----------------------------------------")
    while True:
        amount = int(input("Enter an Amount: "))
        if not 4 <= amount <= 8:
            category = input("Enter a Category: ")
            if category == '':
                print("Invalid Input. Please enter a category.")
                continue

            type_input = input("Enter the type: ")
            if type_input.lower() != "expense":
                print("Please type 'Expense' for income.")
                continue

            date = input("Enter the date: ")
            if not is_valid_date(date):
                print("Please type the date correctly.")
                continue

            transaction = [amount, category, type_input, date]
            transactions.append(transaction)
            save_transactions()

            choice_set = input("Transaction added successfully! Do you want to add a New Transaction? [Y/N]: ")
            if choice_set.lower() == 'y':
                continue
            elif choice_set.lower() == 'n':
                break
            else:
                print("Invalid Entry!! Please try again!")

    # After breaking out of the loop (when choice_set is 'n'), return to the main menu
    main_menu()


def view_transactions():
    while True:
        print("-----------------------------------------")
        print("|\t\t\t View Transactions \t\t\t|")
        print("-----------------------------------------")
        print("1. Show All Income Transactions")
        print("2. Show All Expense Transactions")
        print("3. Back to main menu")
        choice = input("Enter the choice: ")
        if choice == "1":
            view_income_transactions()
        elif choice == "2":
            view_expense_transactions()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
        main_menu()


def view_income_transactions():
    print("------------------------------------------------")
    print("|\t\t\t View Income Transactions \t\t|")
    print("------------------------------------------------")
    for transaction in transactions:
        if transaction[2].lower() == "income":
            print("Amount:", transaction[0])
            print("Category:", transaction[1])
            print("Date:", transaction[3])
            print("-----------------------------------------")


def view_expense_transactions():
    print("------------------------------------------------")
    print("|\t\t\t View Expense Transactions \t\t|")
    print("------------------------------------------------")
    for transaction in transactions:
        if transaction[2].lower() == "expense":
            print("Amount:", transaction[0])
            print("Category:", transaction[1])
            print("Date:", transaction[3])
            print("-----------------------------------------")


def update_transaction():
    print("-----------------------------------------")
    print("|\t\t\t View Transactions \t\t\t|")
    print("-----------------------------------------")
    print("1. Update Income Transactions")
    print("2. Update Expense Transactions")
    print("3. Back to main menu")
    choice = input("Enter the choice: ")
    if choice == "1":
        update_income_transactions()
    elif choice == "2":
        update_expense_transactions()
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice. Please try again.")


def update_income_transactions():
    pass


def update_expense_transactions():
    pass


def delete_transaction():
    pass


def display_summary():
    pass


def main_menu():
    while True:
        load_transactions()
        print("-----------------------------------------")
        print("|\t\t Personal Finance Tracker \t\t|")
        print("-----------------------------------------")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
