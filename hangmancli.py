from sys import exit
from random import choice
def find(stri, ch):
    for i, ltr in enumerate(stri):
        if ltr == ch:
            yield i
def main():
	print("Welcome to hangman")
	word = choice(open("hangmanwordlist.txt").readlines()).replace("\n", "")
	listword = list(word)
	spaces = list("_" * len(word))
	if (" " in word):
		spaceposes = list(find(word, " "))
		for i in spaceposes:
			spaces[i] = " "
	solvedLetters = []
	wrongGuesses = []
	lives = 8
	platform = dict([(7, "_________"),
	(6, "|\n|\n|\n|\n|\n _________"),
	(5, "________\n|\n|\n|\n|\n|\n_________"),
	(4, "________\n|    |\n|   (-)\n|\n|\n|\n_________"),
	(3, "________\n|    |\n|   (-)\n|    |\n|    |\n|\n_________"),
	(2, "________\n|    |\n|   (-)\n|   \|/\n|    |\n|\n_________"),
	(1, "________\n|    |\n|   (XX)\n|   \|/\n|    | \n|   / \ \n_________")])
	wordSolved = False

	print("Your word is: " + "".join(spaces) + ", " + str(len(word.replace(" ", ""))) + " letters long.")
	while not wordSolved:
		letter = str(input("\nGuess a letter: ")).lower()
		if len(letter) == 1 and letter.isalpha():
			if letter in listword:
				if letter in solvedLetters:
					print("You already solved this letter")
				else:
					print("Correct")
					solvedLetters.append(letter)
					if listword.count(letter) > 1:
						print("Good job, your guess came up " + str(listword.count(letter)) + " times!")
					positions = list(find(word, letter))
					for i in positions:
						spaces[i] = letter
					print("Your word is: " + "".join(spaces))
					if spaces == listword:
						wordSolved = True
						print("Congratulations, you won! The word was " + word)
						command = input("Now what would you like to do (quit/exit (q/e), restart/play (r/p)): ")
						if command == "q" or command == "quit" or command == "e" or command == "exit":
							exit()
						if command == "r" or command == "restart" or command == "p" or command == "play":
							return main()
			else:
				if letter in wrongGuesses:
					print("You already guessed this wrong")
				else:
					wrongGuesses.append(letter)
					lives -= 1
					print("Wrong\n\n")
					print(platform[lives])
					print("\nYour word is: " + "".join(spaces))
					if (lives == 1):
						print("You lose :(")
						print("The word was " + word)
						command = input("Now what would you like to do (quit/exit (q/e), restart/play (r/p)): ")
						if command == "q" or command == "quit" or command == "e" or command == "exit":
							exit()
						if command == "r" or command == "restart" or command == "p" or command == "play":
							return main()

		else:
			if (letter.lower() == "solve"):
				solve = input("Oh so you would like to solve huh?: ")
				if (solve.lower() == word):
					print("You got it!")
					wordSolved = True
					print("The word was: " + word)
				else:
					lives -= 1
					print("Wrong\n\n")
					print(platform[lives])
					if (lives == 1):
						print("You lose :(")
						print("The word was " + word)
						command = input("Now what would you like to do (quit/exit (q/e), restart/play (r/p)): ")
						if command == "q" or command == "quit" or command == "e" or command == "exit":
							exit()
						if command == "r" or command == "restart" or command == "p" or command == "play":
							return main()
			else:
				print("Not a letter")
main()
