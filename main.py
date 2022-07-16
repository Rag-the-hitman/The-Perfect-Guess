import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")


print(f"You guessed the number in {guesses} guesses")

with open("F:\\The Perfect Guess\\result.txt", "a") as f:
    f.write(str(guesses) + "\n")

with open("D:\\Github\\public projects\\python\\The Perfect Guess\\highscore.txt", "r") as f:
    highscore = int(f. readlines()[-1])

if(guesses<highscore):
    print("You have just broken the high score!")
    with open("D:\\Github\\public projects\python\\The Perfect Guess\\highscore.txt", "w") as f:
        f.write(str(guesses))