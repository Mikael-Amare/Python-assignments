#!/usr/bin/env python3
"""
Created by: Mikael
Created on: May 2024
This module merges and sorts 2 lists.
"""


import random
from typing import List


def list_merge(numbers_array_1: List[int], numbers_array_2: List[int]) -> List[int]:
    """This function merges 2 lists and sorts them"""
    merged_list = numbers_array_1 + numbers_array_2
    sorted_list = sorted(merged_list)
    return sorted_list


def main():
    """This creates two lists"""
    numbers_array_1 = []
    numbers_array_2 = []

    rows = 4
    columns = 4

    print("List number 1:")
    for _ in range(rows):
        for _ in range(columns):
            a_random_number = random.randint(1, 50)
            print(f"{a_random_number} ", end="")
            numbers_array_1.append(a_random_number)
        print("")

    print("\nList number 2:")
    for _ in range(rows):
        for _ in range(columns):
            a_random_number = random.randint(1, 50)
            print(f"{a_random_number} ", end="")
            numbers_array_2.append(a_random_number)
        print("")

    sorted_list = list_merge(numbers_array_1, numbers_array_2)

    print("\nSorted list:")
    for counter in range(0, 1):
        for number in sorted_list:
            if counter > 0 and counter % 5 == 0:  # Start a new line after every 5 numbers
                print("")
                counter = 0
            print(f"{number} ", end="")
            counter += 1

    print("")


if __name__ == "__main__":
    main()
