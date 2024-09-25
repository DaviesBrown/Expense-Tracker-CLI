import csv
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        # If the file does not exist, create it with a header row
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'date', 'description', 'amount'])  # Header

    def _get_last_id(self):
        """Get the last ID in the CSV file to auto-increment."""
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if len(rows) > 1:
                    return int(rows[-1][0])  # Return the ID of the last record
        except Exception as e:
            print(f"Error reading file: {e}")
        return 0  # Return 0 if no records exist

    def add_expense(self, description, amount):
        """Add a new expense with an auto-incrementing ID."""
        if amount < 0:
            print("Error: Amount cannot be negative.")
            return
        
        last_id = self._get_last_id()
        new_id = last_id + 1
        date = datetime.now().strftime('%Y-%m-%d')

        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_id, date, description, amount])
        print(f"Expense added successfully (ID: {new_id})")

    def delete_expense(self, expense_id):
        """Delete an expense with the given ID."""
        records = self.get_all_expenses()
        updated = False
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'date', 'description', 'amount'])  # Write header again
            for row in records:
                if row[0] != str(expense_id):
                    writer.writerow(row)
                else:
                    updated = True
        if updated:
            print("Expense deleted successfully")
        else:
            print("Error: Expense ID not found.")

    def get_all_expenses(self):
        """Retrieve all expenses from the CSV file."""
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            return list(reader)

    def summary(self):
        """Print the summary of all expenses."""
        total_expenses = sum(float(row[3]) for row in self.get_all_expenses())
        print(f"Total expenses: ${total_expenses:.2f}")

    def monthly_summary(self, month):
        """Print the summary of expenses for a specific month."""
        records = self.get_all_expenses()
        total_monthly = sum(float(row[3]) for row in records if datetime.strptime(row[1], '%Y-%m-%d').month == month)
        print(f"Total expenses for month {month}: ${total_monthly:.2f}")
