"""
a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
"""

def main():
    grocery_dict={}
    while True:
        try:
            grocery_item = input().strip().upper()
        except EOFError:
            print()
            for item in sorted(grocery_dict):
                print(grocery_dict[item], item)
            break
        except KeyError:
            pass
        else:
            if grocery_item in grocery_dict:
                grocery_dict[grocery_item] += 1
            else:
                grocery_dict[grocery_item] = 1



main()
