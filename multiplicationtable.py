def table(n = 12):
	# for row in range(1, n + 1):
	# 	if row > 1:
	# 		line = str(row) + " "
	#
	# 	else:
	# 		line = list(range(row, n + 1))
	# 		print(str(line).replace(",", "").replace("[", "").replace("]", ""))
	line = ""
	for row in range(1, n + 1):
		for column in range(1, n + 1):
			if row == 1:
				line += str(row * column) + "  "
			elif column == 1 and row < 10:
				line += str(row * column) + "  "
			elif column == 2 and row < 5:
				line += str(row * column) + "  "
			elif column == 3 and row < 4:
				line += str(row * column) + "  "
			elif column == 4 and row == 2:
				line += str(row * column) + "  "
			elif column > 9 and row < 10:
				line += str(row * column) + "  "
			else:
				line += str(row * column) + " "
		line += "\n"
	print(line)
table()
