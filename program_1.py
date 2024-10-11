import random
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

def randDice() -> int:
    # Write your logic to generate 2 numbers between 1 and 6 here

    # Sum 2 numbers

    # return sum to calling function
    return random.randint(1,6) + random.randint(1,6)

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.

if __name__ == "__main__":
    average : int = 0
    for x in range(100):
        average += randDice()

    average /= 100

    print(f"Average role: {average}")