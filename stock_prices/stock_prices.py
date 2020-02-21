#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # find highest value
    # find lowest value that is before highest value
    current_min = prices[0]
    current_max = prices[-1]
    current_min_index = 0
    current_max_index = prices.index(prices[-1])

    for i in range(1, len(prices), 1):
        if current_min > prices[i] and i < current_max_index:
            current_min = prices[i]
            current_min_index = i
        for j in range(i + 1, len(prices), 1):
            if current_max < prices[j] and j > current_min_index:
                current_max = prices[j]
                current_max_index = j

    return current_max - current_min


# find_max_profit([10, 7, 5, 8, 11, 9])

if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )
