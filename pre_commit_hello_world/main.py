import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file-name", nargs="+")

    args = parser.parse_args()
    print(args)