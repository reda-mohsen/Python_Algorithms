"""
a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
Format the table using the library’s grid format. If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv, or if the specified file does not exist,
the program should instead exit via sys.exit.
"""
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

from tabulate import tabulate
import sys
import csv

def main():
    read_csv(get_argument())

def read_csv(csv_file):
    pizzas=[]
    if check_file(csv_file):
        try:
            with open(csv_file) as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    pizzas.append(row)
                print(tabulate(pizzas[1:],headers=pizzas[0],tablefmt="grid"))
        except IOError:
            sys.exit("File does not exist")
    else:
         sys.exit("Not a CSV file")

def get_argument():
    try:
        if len(sys.argv) <2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) >2:
            sys.exit("Too many command-line arguments")
        else:
            return sys.argv[1]
    except IndexError:
          sys.exit()

def check_file(csv_file):
    return csv_file.endswith(".csv")

if __name__ == "__main__":
    main()
