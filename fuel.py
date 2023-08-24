"""
a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs,
as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank
is essentially empty. And if 99% or more remains,
output F instead to indicate that the tank is essentially full.
"""

def main():
    fraction = get_fraction("Fraction: ")
    percentage = round(fraction*100)
    if percentage < 1:
        print ("E")
    elif percentage>99:
        print("F")
    else:
        print(f"{percentage}%")

def get_fraction(prompt):
    while True:
        try:
            fraction = input(prompt).strip().split("/")
            if len(fraction) == 2:
                x = int(fraction[0])
                y = int(fraction[1])
                if x>y:
                    continue
                else:
                    return x/y
            else:
                continue
        except (ValueError, ZeroDivisionError):
            pass
        
main()
