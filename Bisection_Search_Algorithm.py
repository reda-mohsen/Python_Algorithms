# Author: Reda Mohsen

# Bisection Search Algorithm
print("Searching for a number from 0 to 100")
print("Please think of an integer number between 0 and 100!")
# for example number = 12
low = 0
high = 100
medium = int((low+high)/2) # medium initially = 50
state = True

# Define check_guess function
def check_guess(medium):
    # Docstrings
    """
        This function takes the medum and ask the user if it is the number he guesses!
        Input: medium, Type: Integer
        Output: c if the guess is correct,
        h if the guess is higher,
        l if the guess is lower than the medium
    """
    print("Is you secret number = "+ str(medium)+" ?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly \n")
    return guess

counter = 0
while state: # true, true, false
    guess = check_guess(medium)
    if (guess == 'c'):
        print("Game over. Your secret number is "+ str(medium)+" !!")
        state = False
    elif (guess == 'l'): # true, true
        high = medium # high = 50, high = 25
        medium = (low+high)//2 # medium = 25, medium = 12
        counter +=1 # counter = 1, counter = 2
    elif (guess=='h'):
        low = medium
        medium = (low+high)//2
        counter +=1
    
Output = str(medium) + " is found in " + str(counter+1) + " iteration"
print(Output) # print with medium = 12 and counter = 2
