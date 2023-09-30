"""
+Prompts the user for a level n. If the user does not input 1, 2, or 3, the program should prompt again.
+Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
 digits. No need to support operations other than addition (+).
+Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE
 and prompt the user again, allowing the user up to three tries in total for that problem.
 If the user has still not answered correctly after three tries, the program should output the correct answer.
+The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

import random


def main():
    level = get_level()
    error = 3
    score = 10

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                if error > 0:
                    print("EEE")
                    error -=1
                    if error ==0:
                        print(f"{x} + {y} = {x+y}")
                        score -= 1
                        error = 3
                        break
                    else:
                        continue
                else:
                    break
            else:
                if error > 0:
                    if answer == x+y:
                        break
                    else:
                        print("EEE")
                        error -=1
                        if error ==0:
                            print(f"{x} + {y} = {x+y}")
                            score -= 1
                            error = 3
                            break
                        else:
                            continue
                else:
                    break

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue



def generate_integer(level):
    if level == 1:
        integer = random.randint(0,9)
    elif level == 2:
        integer = random.randint(10,99)
    elif level == 3:
        integer = random.randint(100,999)
    return integer

if __name__ == "__main__":
    main()
