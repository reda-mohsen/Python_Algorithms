"""
function convert expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format
(i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
"""


import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(hours):
    try:
        if matches := re.search(r"^(\d\d?(?::\d{2})?) (AM|PM)? to (\d\d?(?::\d{2})?) (AM|PM)?$",hours):
            from_hour, from_half = matches.group(1), matches.group(2)
            to_hour, to_half = matches.group(3), matches.group(4)
            from_hour, from_min = split_hour(from_hour)
            to_hour, to_min = split_hour(to_hour)

            if int(from_hour) < 0 or int(from_hour) > 12:
                raise ValueError("ValueError")
            elif int(to_hour) < 0 or int(to_hour) > 12:
                raise ValueError("ValueError")
            elif int(from_min) < 0 or int(from_min) > 59:
                raise ValueError("ValueError")
            elif int(to_min) < 0 or int(to_min) > 59:
                raise ValueError("ValueError")
            else:
                if from_half == "AM":
                    if len(from_hour)==2 and not from_hour=="12" :
                        from_hour = f"{from_hour}:{str(to_min)}"
                    elif len(from_hour)==2 and from_hour=="12" :
                        from_hour = f"00:{str(from_min)}"
                    elif len(from_hour)==1:
                        from_hour = f"0{from_hour}:{str(from_min)}"
                elif from_half == "PM":
                    if from_hour == "12":
                        from_hour = f"{str(from_hour)}:{str(from_min)}"
                    else:
                        from_hour = int(from_hour)+12
                        from_hour = f"{str(from_hour)}:{str(from_min)}"
                if to_half == "AM":
                    if len(to_hour)==2 and not to_hour=="12" :
                        to_hour = f"{to_hour}:{str(to_min)}"
                    elif len(to_hour)==2 and to_hour=="12" :
                        to_hour = f"00:{str(to_min)}"
                    elif len(to_hour)==1:
                        to_hour = f"0{to_hour}:{str(to_min)}"
                elif to_half == "PM":
                    if to_hour == "12":
                        to_hour = f"{str(to_hour)}:{str(to_min)}"
                    else:
                        to_hour = int(to_hour)+12
                        to_hour = f"{str(to_hour)}:{str(to_min)}"
                return f"{from_hour} to {to_hour}"
        else:
            raise ValueError("ValueError")
    except ValueError:
        sys.exit("ValueError")

def split_hour(hour):
    if ":" in hour:
        return hour.split(":")
    else:
        return [hour,"00"]

if __name__ == "__main__":
    main()