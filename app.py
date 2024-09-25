import argparse

from add import setup_add_parser
from delete import setup_delete_parser
from list import setup_list_parser
from summary import setup_summary_parser

from expense_tracker import ExpenseTracker

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Add command
    setup_add_parser(subparsers)

    # Delete command
    setup_delete_parser(subparsers)

    # List command
    setup_list_parser(subparsers)

    # Summary command
    setup_summary_parser(subparsers)

    args = parser.parse_args()
    tracker = ExpenseTracker()

    option = args.command

    match option:
        case 'add':
            tracker.add_expense(args.description, args.amount)
        case 'delete':
            tracker.delete_expense(args.id)
        case 'list':
            print("ID  Date       Description  Amount")
            for row in tracker.get_all_expenses():
                print(f"{row[0]}   {row[1]}  {row[2]}        ${row[3]}")
        case 'summary':
            if args.month:
                tracker.monthly_summary(args.month)
            else:
                tracker.summary()
        case default:
            parser.print_help()

if __name__ == '__main__':
    main()
