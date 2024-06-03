#!/usr/bin/env python3
"""
Created by: Mikael Amare
Created on: May 2024
This program is calculates the fibonacci sequence
"""


def main():
    """This module calculates the fibonacci sequence
    to given number of terms"""
    counter = 2
    fibbonacci_number = 0
    fibbonacci_number1 = 0
    fibbonacci_number2 = 1
    terms = input("Enter the number of terms: ")

    while True:
        try:
            terms_int = int(terms)
        except ValueError:
            terms = input("You did not enter a number, try again: ")
        else:
            break
    if terms_int == 0:
        print("\nNo terms to print")
        print("\nDone.")
        return
    if terms_int == 1:
        print("\n0")
        print("\nDone.")
        return
    print("\n0")
    print("1")
    while counter < terms_int:
        fibbonacci_number = fibbonacci_number1 + fibbonacci_number2
        fibbonacci_number1 = fibbonacci_number2
        fibbonacci_number2 = fibbonacci_number
        counter = counter + 1
        print(fibbonacci_number)

    print("\nDone.")


if __name__ == "__main__":
    main()
