"""
a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py,
or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.)
Assume that any line that only contains whitespace is blank.
"""

import sys

def main():
    #create_file()
    print(count_loc(get_argument()))

def create_file():
    with open("hello.py", "a") as file:
        file.write("# Say hello\n\n")
        file.write("name = input('What's your name? ')\n")
        file.write("print(f'hello, {name}')")

def count_loc(python_file):
     if check_file(python_file):
        loc = 0
        try:
            with open(python_file) as file:
                for line in file:
                    loc += 1
                    if line.strip().startswith("#") or len(line.rstrip())<1:
                        loc -= 1
            return loc
        except IOError:
            sys.exit("File does not exist")
     else:
         sys.exit("Not a Python file")

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

def check_file(python_file):
    return python_file.endswith(".py")

if __name__ == "__main__":
    main()






