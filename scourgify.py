"""
+ Expects the user to provide two command-line arguments:
    - the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    - the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
+ Converts that input to that output, splitting each name into a first name and last name.
  Assume that each student will have both a first name and last name.
+ If the user does not provide exactly two command-line arguments, or if the first cannot be read,
  the program should exit via sys.exit with an error message.
"""
# wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

import csv
import sys

def main():
    csv_1, csv_2 = get_arguments()
    if check_csv_file(csv_1) and check_csv_file(csv_2):
        order_csv(split(csv_1), csv_2)
    else:
        sys.exit("Not a CSV file")

def split(before_csv):
    new_data = []
    try:
        with open(before_csv) as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                last,first = row["name"].split(", ")
                new_data.append({"first":first,"last":last,"house":row["house"]})
            return new_data
    except IOError:
         sys.exit(f"Could not read {before_csv}")

def order_csv(data, after_csv):
    fieldnames = ["first", "last", "house"]
    try:
        with open(after_csv, "w") as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for student in data:
                csv_writer.writerow({"first": student["first"], "last": student["last"], "house":student["house"]})

    except IOError:
         sys.exit()

def check_csv_file(csv_file):
    return csv_file.endswith(".csv")

def get_arguments():
    try:
        if len(sys.argv) <3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) >3:
            sys.exit("Too many command-line arguments")
        else:
            return sys.argv[1], sys.argv[2]
    except IndexError:
          sys.exit()

if __name__ == "__main__":
    main()

