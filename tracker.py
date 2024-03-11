import json

# Global List
transactions = []


# load all transactions
def load_transactions():
    # read the data in the json file
    with open("Data.json", 'r') as f:
        trans_data = json.load(f)

        for x in trans_data:
            print(x)


# Save the transactions
def save_transactions():
    # write the data in the json file
    with open("Data.json", "w") as f:
        json.dump(transactions, f)

# Add The Income.
def add_income():
    print("-----------------------------------------")
    print("|\t\t\t Add Income \t\t\t|")
    print("-----------------------------------------")
    while True:



def add_expense():
    pass


# add the transactions (main)
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
            main_menu()
        else:
            print("Invalid choice. Please try again.")
            main_menu()


def view_transactions():
    pass


def update_transaction():
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
