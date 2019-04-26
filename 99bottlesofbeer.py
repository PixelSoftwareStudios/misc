for x in range(99, 0, -1):
	if (x == 1):
		print("1 bottle of beer on the wall, 1 bottle of beer.")
		bottles = "1 bottle of beer on the wall, 1 bottle of beer."
		print("Take one down and pass it around, no more bottles of beer on the wall.\n")
		bottles = "Take one down and pass it around, no more bottles of beer on the wall."
		print("No more bottles of beer on the wall, no more bottles of beer.")
		bottles = "No more bottles of beer on the wall, no more bottles of beer."
		print("Go to the store and buy some more, 99 bottles of beer on the wall.")
		bottles = "Go to the store and buy some more, 99 bottles of beer on the wall."
	else:
		print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
		bottles = str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer."
		if (x == 2):
			print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
			bottles = "Take one down and pass it around, 1 bottle of beer on the wall."
		else:
			print("Take one down and pass it around, " + str(x - 1) + " bottles of beer on the wall.\n")
			bottles = "Take one down and pass it around, " + str(x - 1) + " bottles of beer on the wall."
