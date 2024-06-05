#!/usr/bin/env python3
"""
Created by: Mikael Amare
Created on: Feb 2024
This module calculates the area of a triangle with user given data
"""


def calculation(base_float: float, height_float: float) -> float:

    # Process
    area = (base_float * height_float) / 2

    return area

    # Output


def main():
    """this function calculates the area of the triangle based on user input"""
    # Input

    while True:
        base_length = input("\nEnter the height of the triangle (cm): ")
        height = input("Enter the base length of the triangle (cm): ")

        # Added try and catch so it wont crash
        try:
            base_float = float(base_length)
            height_float = float(height)
            break  # Break out of the loop if inputs are valid
        except ValueError:
            print("That was not a valid input. Please try again:")

    area = calculation(base_float, height_float)

    print(f"\nThe area of the triagnle is {area:.2f} cm².")
    print("\nDone.")


if __name__ == "__main__":
    main()
