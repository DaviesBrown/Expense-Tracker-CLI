import argparse
from add import setup_add_parser
from delete import setup_delete_parser
from list import setup_list_parser


main_parser = argparse.ArgumentParser(description='Expense tracker application')
subparsers = main_parser.add_subparsers(dest='command', help='Available commands')

setup_add_parser(subparsers)
setup_delete_parser(subparsers)
setup_list_parser(subparsers)

args = main_parser.parse_args()

match args.command:
        case 'add':
            print(f"Adding expense: {args.description} with amount {args.amount}")
        case 'update':
            ...
        case 'list':
            print(f"Listing expenses with filter: {args.filter}")
        case 'delete':
            print(f"Deleting expense with ID: {args.id}")
        case 'summary':
            ...
