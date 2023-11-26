#!/usr/bin/env python3

import sys

def factorize_number(n):
    """Factorize a number into two smaller numbers."""
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize_number(number)
            if factors:
                print("{}={}*{}".format(number, factors[0], factors[1]))

if __name__ == "__main__":
    main()

