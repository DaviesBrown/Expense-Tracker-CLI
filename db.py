import csv
import os

class CSVStorage:
    def __init__(self, filename):
        self.filename = filename 
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Date', 'Description', 'Amount'])

    def _get_last_id(self):
        """Get the last ID in the CSV file to auto-increment."""
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if len(rows) > 1:
                    return int(rows[-1][0])
        except Exception as e:
            print(f"Error reading file: {e}")
        return 0

    def add_record(self, record):
        """Add a new record to the CSV file."""
        last_id = self._get_last_id()
        new_id = last_id + 1

        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            record.insert(0, new_id)
            writer.writerow(record)
        print(f"Record {record} added successfully with ID {new_id}.")


    def get_all_records(self):
        """Retrieve all records from the CSV file."""
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            records = list(reader)
        return records

    def get_record_by_id(self, record_id):
        """Retrieve a specific record by ID."""
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == str(record_id):
                    return row
        return None

    def update_record(self, record_id, updated_record):
        """Update a record with the given ID."""
        records = self.get_all_records()
        updated = False
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Date', 'Description', 'Amount'])
            for row in records:
                if row[0] == str(record_id):
                    writer.writerow(updated_record)
                    updated = True
                else:
                    writer.writerow(row)
        if updated:
            print(f"Record with ID {record_id} updated successfully.")
        else:
            print(f"Record with ID {record_id} not found.")

    def delete_record(self, record_id):
        """Delete a record with the given ID."""
        records = self.get_all_records()
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Date', 'Description', 'Amount'])
            for row in records:
                if row[0] != str(record_id):
                    writer.writerow(row)
        print(f"Record with ID {record_id} deleted successfully.")

storage = CSVStorage('expense.csv')
