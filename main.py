
import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    title = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['title']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ₹{total:.2f}")


def show_categories(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = (
            totals.get(category, 0) + expense["amount"]
        )

    if not totals:
        print("No expenses to categorize.")
        return

    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spending")
        print("4. Spending by category")
        print("5. Delete expense")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_categories(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
