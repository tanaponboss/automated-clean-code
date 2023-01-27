# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse


def find_max_key(counter: dict) -> [str, int]:
    """High level support for doing this and that."""
    temp_key = ""
    temp_counter = 0
    winner = 0
    for k, v in counter.items():
        if v > winner:
            temp_key = k
            temp_counter = v
            winner = v
    return temp_key, temp_counter


def find_min_key(counter: dict) -> [str, int]:
    """High level support for doing this and that."""
    temp_key = ""
    temp_counter = 0
    winner = 100000
    for k, v in counter.items():
        if v < winner:
            temp_key = k
            temp_counter = v
            winner = v
    return temp_key, temp_counter


def main():
    """High level support for doing this and that."""
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    args = parser.parse_args()
    counter = {}

    # fill up histogram
    with open(args.fname, "r") as f:
        for line in f:
            line = line.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 0

    max_key, max_counter = find_max_key(counter)
    min_key, min_counter = find_min_key(counter)

    print(f"Min Key = {min_key} with count = {min_counter}")
    print(f"Max Key = {max_key} with count = {max_counter}")


if __name__ == "__main__":
    main()
