"""
prompts the user for an email address via input and then prints Valid or Invalid,
respectively, if the input is a syntatically valid email address.
"""
import validators

def main():
    print(is_valid(input("What's your email address? ").strip()))

def is_valid(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()