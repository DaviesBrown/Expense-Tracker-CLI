import argparse

def setup_summary_parser(subparsers):
    """
    Setup for the 'summary' subcommand
    """
    summary_parser = subparsers.add_parser('summary', help='Summarize all expenses')
    add_parser.add_argument('--month', type=int, required=False, help='Specific month (of current year)')
    return summary_parser
