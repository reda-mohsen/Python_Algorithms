"""
a function called parse that expects a str of HTML as input, extracts any YouTube URL that's the value of a src attribute
of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str.
Expect that any such URL will be in one of the formats below.
Assume that the value of src will be surrounded by double quotes.
And assume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None.
"""

import re

def main():
    print(parse(input("HTML: ").strip()))

def parse(html):
    if match := re.search(r"^<iframe.+src=(?:\"|\')https?://(?:www\.)?youtube\.com/embed/(\w+)(?:\"|\').*></iframe>$", html, re.IGNORECASE):
        return "https://youtu.be/" + match.group(1)

if __name__ == "__main__":
    main()