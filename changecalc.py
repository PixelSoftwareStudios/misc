import math
def main(change):
	#A dictionary that holds the values
	result = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}
	#Making sure that the money given is a float
	change = float(change)
	# The amount of quarters is the floor of how many quarters you can fit in change (change / 0.25)
	result["quarters"] = math.floor(change / 0.25)
	# The amount of dimes is the floor of how many dimes you can fit in the change minus the quarters
	result["dimes"] = math.floor((change - (result["quarters"] * 0.25)) / 0.10)
	# The amount of nickels is the floor of how many nickels you can fit in the change minus the quarters and the dimes
	result["nickels"] = math.floor((change - ((result["quarters"] * 0.25) + (result["dimes"] * 0.10))) / 0.05)
	# The amount of nickels is the floor of how many pennies you can fit in the change minus the quarters and the dimes and the nickels
	result["pennies"] = math.floor((change - ((result["quarters"] * 0.25) + (result["dimes"] * 0.10) + (result["nickels"] * 0.05))) / 0.01)
	return "You need " + str(result["quarters"]) + " quarters, " + str(result["dimes"]) + " dimes, " + str(result["nickels"]) + " nickels, and " + str(result["pennies"]) + " pennies."
while True:
	print(main(input()))
