from random import randint
totalGuesses = []
def main():
	number = randint(1, 100)
	guess = 0
	guesses = 0
	while guess != number:
		guess = input("Guess: ")
		if guess:
			if guess.isdigit():
				guess = int(guess)
				guesses += 1
				if (guess > number):
					print("Lower!")
				if (guess < number):
					print("Higher!")
	print("Congratulations! The number was " + str(number))
	print("It took you " + str(guesses) + " guesses to find this number")
	totalGuesses.append(guesses)
	print("Your statistical average number of guesses: " + str(sum(totalGuesses)//len(totalGuesses)))
	again = input("Would you like to play again? (y/n): ")
	if again == "y" or again == "yes":
		print("\n\n")
		return main()
main()
