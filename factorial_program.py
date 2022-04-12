#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is a factorial calculator


def main():
    # this function calculates the factorial
    counter = 1
    sum_number = 1
    # input
    number_as_string = input("Enter a positive integer: ")
    # process & output
    print("")
    try:
        number_as_int = int(number_as_string)
        if number_as_int == 0:
            print("0! = 1")
        elif number_as_int < 0:
            print("undefined")
        else:
            while counter <= number_as_int:
                sum_number = sum_number * counter
                counter = counter + 1
            print("{0}! = {1}.".format(number_as_int, sum_number))
    except Exception:
        print("That is not a integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
