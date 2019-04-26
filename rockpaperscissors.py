from random import choice
moveSet = ["rock", "paper", "scissors"]
winning = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
winningAbbr = [("r", "s"), ("s", "p"), ("p", "r")]
score = {"player": 0, "computer": 0}
def main():
	playerMove = input("Your move (rock/paper/scissors): ")
	computerMove = choice(moveSet)
	winner = "Nobody"
	for w in winningAbbr:
		if playerMove == w[0]:
			if computerMove == w[1]:
				winner = "You"
				score["player"] = score["player"] + 1
		if computerMove == w[0]:
			if playerMove == w[1]:
				winner = "Computer"
				score["computer"] = score["computer"] + 1

	for w in winning:
		if playerMove == w[0]:
			if computerMove == w[1]:
				winner = "You"
				score["player"] = score["player"] + 1
		if computerMove == w[0]:
			if playerMove == w[1]:
				winner = "Computer"
				score["computer"] = score["computer"] + 1

	print("You played " + playerMove + ", Computer played " + computerMove)
	print(winner + " won!")
	print("Score: You: " + str(score["player"]) + " / Computer: " + str(score["computer"]))
	again = input("Play again?: ")
	if again == "y" or again == "yes":
		print("\n\n")
		return main()
main()
