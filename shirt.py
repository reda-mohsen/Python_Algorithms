"""
+ a program that expects exactly two command-line arguments:
    - in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    - in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
+ The program should then overlay shirt.png (which has a transparent background) on the input after resizing
and cropping the input to be the same size, saving the result as its output.
+ The program should instead exit via sys.exit:
    - if the user does not specify exactly two command-line arguments,
    - if the input's and output's names do not end in .jpg, .jpeg, or .png, case-insensitively,
    - if the input's name does not have the same extension as the output's name, or
    - if the specified input does not exist.
"""

# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip

from PIL import Image, ImageOps
import sys
import os

def main():
    input, output = get_arguments()
    overlay(input, output)


def overlay(input, output):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(input) as input_image:
            input_image = ImageOps.fit(input_image, size)
            input_image.paste(shirt, mask = shirt)
            input_image.save(output)
    except FileNotFoundError:
        sys.exit("Image does not exist")

def get_arguments():
    try:
        format = [".jpg", ".png",".jpeg"]
        if len(sys.argv) <3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) >3:
            sys.exit("Too many command-line arguments")
        else:
            input, output = sys.argv[1].lower(), sys.argv[2].lower()
            input_file, input_ext = os.path.splitext(input)
            output_file, output_ext = os.path.splitext(output)
            if input_ext not in format:
                sys.exit("Invalid input")
            elif output_ext not in format:
                sys.exit("Invalid output")
            elif input_ext != output_ext:
                sys.exit("Input and output have different extensions")
            else:
                return input, output
    except IndexError:
          sys.exit()

if __name__ == "__main__":
    main()
