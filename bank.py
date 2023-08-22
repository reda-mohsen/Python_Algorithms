"""
a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100.
"""

greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

