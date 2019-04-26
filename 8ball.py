from time import sleep
from random import choice
positiveResponses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]
uncertainResponses = ["Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
negativeResponses = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def main():
	question = input("What is your question?: ")
	if "is this the krusty krab" in question.lower():
		return print("NO THIS IS PATRICK")
	sleep(1)
	print("Thinking...")
	sleep(2)
	response = choice(choice([positiveResponses, uncertainResponses, negativeResponses]))
	print(response)
	again = input("Ask again?: ")
	if again == "y" or again == "yes":
		print("\n\n")
		return main()
main()
