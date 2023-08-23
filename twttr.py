"""
a program that prompts the user for a str of text and then outputs that same text
but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""

def main():
    text = input("Input: ").strip()
    vowels = ['A', 'E', 'I', 'O', 'U']
    lower_vowels = []
    for i in range(len(vowels)):
        lower_vowels.append(vowels[i].lower())

    for character in text:
        for i in range(len(vowels)):
            if character == vowels[i] or character == lower_vowels[i]:
                text = text.replace(character,"")

    print ("Output:", text)

main()