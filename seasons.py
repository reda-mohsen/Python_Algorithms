"""
prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes,
    rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words.
    Since a user might not know the time at which they were born.
assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
assume that the current time is also midnight. In other words, even if the user runs the program at noon,
assume that it's actually midnight, on the same date.
"""
# 2000-09-29

from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    print(convert(input("Date of Birth: ").strip()))


def convert(my_date):
    try:
        current_date = date.today()
        my_date = date.fromisoformat(my_date)
        days = current_date - my_date
        minutes = days.days*24*60
        minutes = p.number_to_words(minutes, andword="").capitalize()
        return minutes + ' minutes'
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()