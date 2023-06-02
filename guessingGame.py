# Guessing game: create a program that generates random number
# and lets' user guess it

# Imports
import random

# Greetings and instructions for player
print("Hello, would you like to play a game?")

playingGame = input("y/n: ")
while playingGame == "y":
    # Generating random number and assigning it to variable
    randomNumber = random.randint(1,100)
    print("I thought about a number between 1 and 100.")
    print("Can you guess it?")

    #Asking player for his number
    playersNumber = input("Your number is: ")

    # Checking if given number is equal to randomised number
    if randomNumber == int(playersNumber):
        print("That's correct! You've made it!")
    else:
        print(f"Ohh you didn't make it. My number was {randomNumber}")
    
    #Checking if player still wants to play
    print("Do you want to play again?")
    playingGame = input("y/n: ")