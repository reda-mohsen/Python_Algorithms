"""
In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :)
 converted to 🙂 (otherwise known as a slightly smiling face)
 and any :( converted to 🙁 (otherwise known as a slightly frowning face).
 All other text should be returned unchanged.
"""
def main():
    input_str = input("Enter a message ends with a slightly smiling/frowning face: ")
    str_to_print = convert_to_emoji(input_str)
    print(str_to_print)

def convert_to_emoji(input_string):
    result = input_string.replace(":)","🙂",len(input_string)).replace(":(","🙁",len(input_string))
    return result
main()
