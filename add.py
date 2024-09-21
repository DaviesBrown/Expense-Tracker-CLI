import argparse

def setup_add_parser(subparsers):
    """
    Setup for the 'add' subcommand
    """
    add_parser = subparsers.add_parser('add', help='Add an expense with a description and amount')
    add_parser.add_argument('--description', type=str, required=True, help='Description of the expense')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the expense')
    return add_parser
