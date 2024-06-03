#!/usr/bin/env python3
"""
Created by: Mikael
Created on: Mar 2024
This module checks if triangle is equilateral, isocoles, or scalene.
"""


def main():
    """Checks if triangle is equilateral, isocoles, or scalene."""
    # input
    side_1 = int(input("Enter sidelength: "))
    side_2 = int(input("Enter second sidelength: "))
    side_3 = int(input("Enter third sidelength: "))

    # process & output
    if side_1 == side_2 == side_3:
        print("\nIt is an equilateral.")
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("\nIt is an isosceles.")
    else:
        print("\nIt is a scalene.")

    print("\nDone.")


if __name__ == "__main__":
    main()
