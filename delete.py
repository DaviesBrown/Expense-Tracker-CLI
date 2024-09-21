import argparse

def setup_delete_parser(subparsers):
    """
    Setup for the 'delete' subcommand
    """
    delete_parser = subparsers.add_parser('delete', help='Delete an expense by ID')
    delete_parser.add_argument('--id', type=int, required=True, help='ID of the expense to delete')
    return delete_parser
