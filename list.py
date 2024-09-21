import argparse

def setup_list_parser(subparsers):
    """
    Setup for the 'list' subcommand
    """
    list_parser = subparsers.add_parser('list', help='List all expenses')
    return list_parser
