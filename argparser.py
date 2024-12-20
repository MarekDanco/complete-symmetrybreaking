"""Parse command line arguments."""

import argparse


def arg_parser():
    """Returns ArgumentParser object equipped with defined arguments."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "domain",
        help="domain size",
        type=int,
    )
    arg_parser.add_argument(
        "filename",
        help="filename with input formula",
        default="-",
        nargs="?",
        type=str,
    )
    arg_parser.add_argument(
        "-p",
        "--permutations",
        help="encode minimality under all permutations",
        default=False,
        action="store_true",
    )
    arg_parser.add_argument(
        "-t",
        "--transpositions",
        help="encode minimality under transpositions only",
        default=False,
        action="store_true",
    )
    arg_parser.add_argument(
        "-r",
        "--rows",
        help="encode minimality with respect to cells ordered by rows",
        default=False,
        action="store_true",
    )
    arg_parser.add_argument(
        "-c",
        "--concentric",
        help="encode minimality with respect to concentric ordering",
        default=False,
        action="store_true",
    )
    arg_parser.add_argument(
        "-d",
        "--diagonal",
        help="encode minimality with respect to diagonal ordering",
        default=False,
        action="store_true",
    )
    arg_parser.add_argument(
        "-lnh",
        help="break symmetries using the Least Number Heuristic",
        default=False,
        action="store_true",
    )
    arg_parser.add_argument(
        "-a",
        "--approx",
        help="approximate the number of models",
        default=False,
        action="store_true",
    )
    arg_parser.add_argument(
        "-s",
        "--solver",
        help="name of  the SAT solver, set to Cadical195 by default",
        default="cd19",
        nargs="?",
        type=str,
    )
    return arg_parser
