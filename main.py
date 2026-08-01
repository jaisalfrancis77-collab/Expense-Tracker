import json
import os

FILE_NAME = "data.json"

# Load existing expenses
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
else:
    expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "id": len(expenses) + 1,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully.")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\nID\tDescription\tAmount")
            for expense in expenses:
                print(f"{expense['id']}\t{expense['description']}\t₹{expense['amount']}")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expense: ₹{total}")

    elif choice == "4":
        delete_id = int(input("Enter Expense ID to delete: "))

        found = False
        for expense in expenses:
            if expense["id"] == delete_id:
                expenses.remove(expense)
                found = True
                print("Expense deleted successfully.")
                break

        if not found:
            print("Expense ID not found.")

    elif choice == "5":
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expenses saved successfully.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")