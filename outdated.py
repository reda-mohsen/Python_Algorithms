"""
In a file called outdated.py, implement a program that prompts the user for
a date, anno Domini, in month-day-year order,formatted like 9/8/1636
or September 8, 1636.Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days.
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input("Date: ").strip().capitalize()
            if is_valid_date(date):
                (year,month,day) = convert_to_iso(date)
                year = int(year)
                month = int(month)
                day = int(day)
                print(f"{year:04}-{month:02}-{day:02}")
                break
            
        except ValueError:
            pass
        except KeyError:
            pass
            
            
        
def is_valid_date(date):
    try:
        for month_name in months:
            if date.startswith(month_name):
                (month_day, year) = date.split(", ")
                (month, day) = month_day.split(" ")
                day = int(day)
                year = int(year)
                if month_name==month and day>0 and day<31 and year>0:
                    return True
                else:
                    return False
                break
            else:
                continue

        (month,day,year) = date.split("/")
        day = int(day)
        month = int(month)
        year = int(year)
        if month>0 and month<12 and day>0 and day<31 and year>0:
            return True
        else:
            return False
        
    except ValueError:
        return False
        
    
def convert_to_iso(date):
    try:
        for i in range(len(months)):
            if date.startswith(months[i]):
                (month_day, year) = date.split(", ")
                (month, day) = month_day.split(" ")
                month = str(i+1)
                return (year,month,day)
            else:
                continue

        (month,day,year) = date.split("/")
        return (year,month,day)
        
    except ValueError:
        return False
    
    

main()
