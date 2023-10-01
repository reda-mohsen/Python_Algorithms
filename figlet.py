"""
+Expects zero or two command-line arguments:
    -Zero if the user would like to output text in a random font.
    -Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
     and the second of the two should be the name of the font.
+Prompts the user for a str of text.
+Outputs that text in the desired font.
+If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
 the program should exit via sys.exit with an error message.
"""
#pip install pyfiglet

from pyfiglet import Figlet
import sys
import random

fonts = ["slant","rectangles","alphabet","3-d", "3x5", "5lineoblique", "acrobatic",
          "alligator","avatar", "banner", "barbwire", "basic", "bell", "big",
          "bigchief","block","bubble","bulbhead","catwalk","chunky","cosmike","diamond"]

try:
    if len(sys.argv) == 1:
        input = input("Input: ")
        random_font = random.choice(fonts)
        f = Figlet(font=random_font)
        print("Output: ")
        print(f.renderText(input))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            found = False
            for font in fonts:
                if sys.argv[2] == font:
                    found = True
            if found:
                input = input("Input: ")
                f = Figlet(font=sys.argv[2])
                print("Output: ")
                print(f.renderText(input))
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
         sys.exit("Invalid usage")

except IndexError:
    sys.exit("Invalid usage")
except KeyError:
    sys.exit("Invalid usage")
