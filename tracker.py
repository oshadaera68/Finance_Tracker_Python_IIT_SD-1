# import the json and os module
import json

# import the datetime module
from datetime import datetime

# Global List
transactions = []


# load all transactions
def load_transactions():
    try:
        with open("data.json", "r") as file:
            trans_data = json.load(file)  # load all transactions in the file
    except FileNotFoundError:
        trans_data = []
    except json.JSONDecodeError:
        trans_data = []
    except Exception as e:
        print(f"Error loading transactions: {e}")
        trans_data = []

    transactions.clear()
    transactions.extend(trans_data)

    for data in transactions:
        print(data)


# Save the transactions
def save_transactions():
    # write the data in the json file
    with open("data.json", "w") as file:
        json.dump(transactions, file)  # getting the string for default and indentation in 2.


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
    print("---------------------------------")
    print("|\t\t Add Transaction \t\t|")
    print("---------------------------------")

    # user inputs with validation
    while True:
        try:
            amount = int(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    category = input("Enter the category: ")

    # Validating type input
    while True:
        type_input = input("Enter the Type (Income/Expense): ")
        # it means you entered the Income, income is valid and Expense, expense is valid and other typing is not valid.
        if type_input not in ['Income', 'Expense', 'income', 'expense']:
            print("Invalid input. Type must be 'Income' or 'Expense'.")
            continue
        break

    date = input("Enter the Date: ")

    # Validating date format
    while True:
        try:
            is_valid_date(date)  # validating the date using function.
            break
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            date = input("Enter the Date: ")

    # adding the transactions
    add = [len(transactions) + 1, amount, category, type_input, date]
    transactions.append(add)
    save_transactions()
    choice = input("Transaction Completed. Do you want to add the another Transaction? [Y/N]:")
    if choice == "y" or choice == "Y":
        add_transaction()
    elif choice == "n" or choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# Show all transactions (main)
def view_transactions():
    print("---------------------------------")
    print("|\t\t View Transactions \t\t|")
    print("---------------------------------")
    # check the Any Transactions for here.
    if not transactions:
        print("No transactions found.")
        return

    # Showing the data in tabular format
    print("-" * 60)
    print("| {:<3} | {:>10} | {:<15} | {:<6} | {:<10} |".format("ID", "Amount", "Category", "Type", "Date"))
    print("-" * 60)
    for trans_list in transactions:
        transaction_id, amount, category, transaction_type, date = trans_list
        print(
            "| {:<3} | {:>10.2f} | {:<15} | {:<6} | {:<10} |".format(transaction_id, amount, category, transaction_type,
                                                                     date))
    print("-" * 60)


# Update Transactions
def update_transaction():
    print("-------------------------------------")
    print("|\t\t Update Transactions \t\t|")
    print("-------------------------------------")
    # check the existing the id for the before update process
    id = int(input("Enter the transaction Id: "))
    if id < 1 or id > len(transactions):
        print("ID is not valid. Please Try again.")
        return

    tran_update = transactions[id - 1]

    # exception handling
    try:
        # print the selected transaction
        print(f"{tran_update[0]}  {tran_update[1]}  {tran_update[2]}  {tran_update[3]}  {tran_update[4]}")
    except IndexError:
        print("List index Out of range")

    # list menu
    print("\nWhat do you want to update?")
    print("1. Update the Amount")
    print("2. Update the Category")
    print("3. Update the Type")
    print("4. Update the Date")
    print("5. Cancel")
    choice = input("Enter the number of the field you want to update: ")

    # Update selected field
    while True:
        if choice == "1":
            # If the user input is empty, It retrieved the data in the selected transaction.
            # But if you entered the input, It assigns the value.
            # Others are Same Manner.
            amount = int(input("Enter the new Amount:") or tran_update[1])
            transactions[id - 1][1] = amount
            break
        elif choice == "2":
            category = input("Enter the new category:") or tran_update[2]
            transactions[id - 1][2] = category
            break
        elif choice == "3":
            trans_type = input("Enter the new type:").capitalize() or tran_update[3]
            transactions[id - 1][3] = trans_type
            break
        elif choice == "4":
            date = input("Enter the new date:") or tran_update[4]
            transactions[id - 1][4] = date
            break
        elif choice == "5":
            print("Update is canceled.")
            break
        else:
            print("Invalid choice. Please Try Again!!")
            choice = input("Enter the number of the field you want to update: ")

    save_transactions()  # save the transactions
    choice = input("Update is Completed. Do you want to update the another Transaction? [Y/N]:")
    if choice == "y" or choice == "Y":
        update_transaction()
    elif choice == "n" or choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# Delete Transactions
def delete_transaction():
    global trans_delete
    print("-------------------------------------")
    print("|\t\t Delete Transactions \t\t|")
    print("-------------------------------------")
    id = int(input("Enter the transaction id for delete: "))
    index = 0
    found = False

    while index < len(transactions):
        if transactions[index][0] == id:
            trans_delete = transactions.pop(index)
            found = True
            break
        else:
            index += 1

    if not found:
        print("Invalid Transaction Id.")
        return

    save_transactions()
    # select the choice for the
    choice = input("Transaction deletion is Completed. Do you want to update another Transaction? [Y/N]:")
    if choice == "y" or choice == "Y":
        delete_transaction()  # Recursively call delete_transaction()
    elif choice == "n" or choice == "N":
        main_menu()  # Return to main menu
    else:
        print("Invalid Value. Please Try Again!!")


# Display All Summary
def display_summary():
    print("---------------------------------")
    print("|\t\t Display Summary \t\t|")
    print("---------------------------------")

    income = sum(transaction[1] for transaction in transactions if transaction[3] == "income")
    expenses = sum(transaction[1] for transaction in transactions if transaction[3] == "expense")
    net_balance = income - expenses

    print(f"Total Income: {income:,.2f}")
    print(f"Total Expenses: {expenses:,.2f}")
    print(f"Net Balance: {net_balance:,.2f}")


# Main Menu
def main_menu():
    load_transactions()
    while True:
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
            exit_the_program()
        else:
            print("Invalid choice. Please try again.")


# print("\n")


# Exiting the program
def exit_the_program():
    choice = input("Did you want to exit the System? [Y/N]: ")
    if choice == "y" or choice == "Y":
        print("Program Exited")
        exit()
    elif choice == "n" or choice == "N":
        main_menu()
    else:
        print("Invalid Input.")
        exit(0)


# Runnable Main Constructor
if __name__ == "__main__":
    main_menu()
