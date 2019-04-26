def toSciNot(n):
	if "." in str(n):
		if n < 0:
			num = float(str(n)[1] + "." + str(n)[3])
			multiplier = -10 ** (len(str(n)) - 2)
		else:
			num = float(str(n)[:1] + "." + str(n)[2:])
			multiplier = 10 ** (len(str(n)) - 1)
	else:
		if n < 0:
			num = float(str(n)[1] + "." + str(n)[2])
			multiplier = -10 ** (len(str(n)) - 2)
		else:
			num = float(str(n)[:1] + "." + str(n)[1:])
			multiplier = 10 ** (len(str(n)) - 1)

	print(num * multiplier)
	return str(num) + "x10^" + str(len(str(n)) - 1) if n > 0 else str(num) + "x10^-" + str(len(str(n)) - 2)
def fromSciNot(n):
	return float(n[:n.index("x")]) * (10 ** int(n[n.index("^") + 1:]))
