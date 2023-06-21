import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file-name")

    args = parser.parse_args()
    print(args)