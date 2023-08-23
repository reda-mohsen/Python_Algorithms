"""
A program that prompts the user for the name of a variable in camel case
and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
"""

def main():
    name = get_camel_case_name()
    to_snake_case_name(name)

def get_camel_case_name():
    return input("camelCase: ").strip()

def to_snake_case_name(name):
    for character in name:
        if character.isupper():
            name = name.replace(character,"_" + character)
    camel_case_name = name.lower()
    print("snake_case: ", camel_case_name)

main()
