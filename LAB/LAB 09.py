import csv

class ExpenseTracker:                                             #defining the class
    def __init__(self):
        self.transactions = {'Expense': [], 'Income': []}          #creating a dictionary

    def add_transaction(self, transaction_type, amount, description):          # function for adding the transactions
        self.transactions[transaction_type].append({'Amount': amount, 'Description': description})

    def calculate_total(self, transaction_type):
        return sum(transaction['Amount'] for transaction in self.transactions[transaction_type])   #function for calculating the total

    def export_to_csv(self, filename):                        # creating a csv file
        with open(filename, 'w', newline='') as csvfile:      # writing in the csv file
            fieldnames = ['Type', 'Amount', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction_type in self.transactions:
                for transaction in self.transactions[transaction_type]:
                    writer.writerow({'Type': transaction_type, 'Amount': transaction['Amount'], 'Description': transaction['Description']})

    def load_from_csv(self, filename):                           # loading the csv file
        with open(filename, 'r') as csvfile:                     # opening the file
            reader = csv.DictReader(csvfile)
            for row in reader:                                    
                transaction_type = row['Type']
                amount = float(row['Amount'])
                description = row['Description']
                self.add_transaction(transaction_type, amount, description)

def main():
    tracker = ExpenseTracker()

    # Load data from a CSV file (if it exists)
    csv_filename = 'expense_income.csv'
    try:
        tracker.load_from_csv(csv_filename)
        print("Data loaded from the CSV file.")
    except FileNotFoundError:
        print("No CSV file found. Starting with an empty tracker.")

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Show Total Expense and Income")
        print("4. Export Data to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a description: ")
            tracker.add_transaction('Expense', amount, description)

        elif choice == "2":
            amount = float(input("Enter the income amount: "))
            description = input("Enter a description: ")
            tracker.add_transaction('Income', amount, description)

        elif choice == "3":
            total_expense = tracker.calculate_total('Expense')
            total_income = tracker.calculate_total('Income')
            print(f"Total Expense: {total_expense}")
            print(f"Total Income: {total_income}")

        elif choice == "4":
            tracker.export_to_csv(csv_filename)
            print("Data exported to the CSV file.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
