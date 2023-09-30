"""
+Prompts the user for a level, n.
+If the user does not input a positive integer, the program should prompt again.
+Randomly generates an integer between 1 and n, inclusive, using the random module.
+Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    -If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    -If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    -If the guess is the same as that integer, the program should output Just right! and exit.
"""

from random import randint

while True:
    try:
        number = int(input("Level: "))
    except ValueError:
        pass
    else:
        if number > 0:
            break
        else:
            continue

random_number = randint(1, number)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        else:
            continue


