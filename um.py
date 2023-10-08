"""
function called count that expects a line of text as input as a str and returns,
as an int, the number of times that “um” appears in that text, case-insensitively,
as a word unto itself, not as a substring of some other word.
"""

import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(text):
    um_found = re.findall(r"\b(um)\b", text, re.IGNORECASE)
    return len(um_found)



if __name__ == "__main__":
    main()