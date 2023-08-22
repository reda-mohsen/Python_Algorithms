"""
a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format,
to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
Eat breakfast between 7:00 and 8:00 a.m., lunch between 12:00 and 13:00 p.m.(12-1), and dinner between 18:00 and 19:00 p.m(6-7).
"""

def main():
    time = input("What time is it? ").strip()
    
    if time.endswith("a.m.") or time.endswith("p.m."):
        converted_time = -1
        time_a, apm = time.split(" ")
        converted_time_a = convert(time_a)
    else:
        converted_time_a = -1
        converted_time = convert(time)
        
    if (converted_time >=7.0 and converted_time <=8.0) or (converted_time_a >=7.0 and converted_time_a <=8.0 and apm=="a.m."):
        print ("breakfast time")
    elif (converted_time >= 12.0 and converted_time<=13.0) or ((converted_time_a==1.0 or (converted_time_a >= 12.0 and converted_time_a < 13.0)) and apm=="p.m."):
        print ("lunch time")
    elif (converted_time >= 18.0 and converted_time<= 19.0) or (converted_time_a >= 6.0 and converted_time_a<=7.0 and apm=="p.m."):
        print ("dinner time")
        
def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)/60
    hours = float(hours)
    converted_time = hours+minutes
    return converted_time

if __name__ == "__main__":
    main()
