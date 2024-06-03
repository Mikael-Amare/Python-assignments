#!/usr/bin/env python3
"""
Created by: Mikael Amare
Created on: Feb 2024
This module calculates the area of a triangle with user given data
"""


def main():
    """this function calculates the area of the triangle based on user input"""
    # Input

    base_length = float(input("\nEnter the height of the triangle (cm): "))
    height = float(input("Enter the base length of the triangle (cm): "))

    # Process
    area = (base_length * height) / 2

    # Output
    print(f"\nThe area of the triagnle is {area:.2f} cm².")
    print("\nDone.")


if __name__ == "__main__":
    main()
