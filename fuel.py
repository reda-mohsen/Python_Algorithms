"""
a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs,
as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank
is essentially empty. And if 99% or more remains,
output F instead to indicate that the tank is essentially full.

convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""
import sys

def main():
    fraction = get_fraction("Fraction: ")
    print(gauge(convert(fraction)))

def get_fraction(prompt):
    while True:
        try:
            fraction = input(prompt).strip().split("/")
            if len(fraction) == 2:
                x = int(fraction[0])
                y = int(fraction[1])
                if x>y:
                    continue
                elif y==0:
                    continue
                else:
                    return f"{fraction[0]}/{fraction[1]}"
            else:
                continue
        except ValueError:
            pass

def convert(fraction):
    try:
        fraction = fraction.split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        value = (x/y)*100
    except ValueError:
        raise
    except ZeroDivisionError:
        raise
    else:
        return int(round(value))

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
