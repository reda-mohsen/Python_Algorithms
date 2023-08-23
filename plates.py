"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable …vanity plate; AAA22A would not be acceptable.
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call
(e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    digit_index = 0
    letter_index = 0
    if len(plate)>6 or len(plate)<2 or plate.isspace() or not plate.isalnum():
        return False
    else:
        for i in range(len(plate)):
            if plate[i].isalpha() and not (letter_index<digit_index and i>=2):
                letter_index = i
            elif plate[i].isdigit():
                if (plate[i] == "0" and i==letter_index+1):
                    return False
                else:
                    digit_index = i
            else:
                return False
        if letter_index > digit_index and not letter_index==len(plate)-1:
            return False
        else:
            return True

main()
