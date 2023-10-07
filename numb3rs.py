"""
a function called validate that expects an IPv4 address as input as a str
and then returns True or False, respectively, if that input is a valid IPv4 address or not.
"""

import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    ips = []
    if match := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
        for i in range(4):
            ips.append(match.group(i+1))
        for number in ips:
            if not int(number) >= 0 or not int(number) <=255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()