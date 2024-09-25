import argparse

def setup_summary_parser(subparsers):
    """
    Setup for the 'summary' subcommand
    """
    summary_parser = subparsers.add_parser('summary', help='Summarize all expenses')
    summary_parser.add_argument('--month', type=int, required=False, help='Specify month (1-12) for monthly summary')
    return summary_parser
