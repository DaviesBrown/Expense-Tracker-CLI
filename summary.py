import argparse

def setup_summary_parser(subparsers):
    """
    Setup for the 'summary' subcommand
    """
    summary_parser = subparsers.add_parser('summary', help='Summarize all expenses')
    return summary_parser
