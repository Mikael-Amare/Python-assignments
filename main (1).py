#!/usr/bin/env python3
"""
Created by: Mikael
Created on: Apr 2024
This module checks number of sides to identify the shape.
"""


def main():
    """Checks if the number corresponds to a certain polygon.
    (example: 3 = triangle, 4 = quadrilateral...). It goes up to 20 sides."""
    # input
    side_number = input("Enter number of sides: ")
    # process & output

    try:
        side_int = int(side_number)
    except ValueError:
        print("That is not a number.")
    else:
        if side_int == 3:
            print("This is a triangle.")
        elif side_int == 4:
            print("This is a quadrilateral.")
        elif side_int == 5:
            print("This is a pentagon.")
        elif side_int == 6:
            print("This is a hexagon.")
        elif side_int == 7:
            print("This is a heptagon.")
        elif side_int == 8:
            print("This is an octagon.")
        elif side_int == 9:
            print("This is a nonagon.")
        elif side_int == 10:
            print("This is a decagon.")
        elif side_int == 11:
            print("This is a hendecagon.")
        elif side_int == 12:
            print("This is a dodecagon.")
        elif side_int == 13:
            print("This is a tridecagon.")
        elif side_int == 14:
            print("This is a tetradecagon.")
        elif side_int == 15:
            print("This is a pentadecagon.")
        elif side_int == 16:
            print("This is a hexadecagon.")
        elif side_int == 17:
            print("This is a heptadecagon.")
        elif side_int == 18:
            print("This is an octadecagon.")
        elif side_int == 19:
            print("This is an enneadecagon.")
        elif side_int == 20:
            print("This is an icosagon.")
        elif side_int > 20:
            print("This is a circle.")
        else:
            print("This is an invalid shape.")

    print("\nDone.")


if __name__ == "__main__":
    main()
