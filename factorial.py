from operator import mul
from functools import reduce

def toFactorial(n):
	return reduce(mul, list(range(1, n + 1)), 1)

def printFactorial(n):
	return str(list(range(1, n+1))).replace(", ", " * ").replace("[", "").replace("]", "") + "\n" + str(reduce(mul, list(range(1, n + 1)), 1))

def fromFactorial(n):
	for x in xrange(n):
		 if toFactorial(x) == n:
			 return x
# Like a factorial but 5 ^ 4 ^ 3 ^ 2 ^ 1
def toExponentFactorial(n):
	result = n
	for x in range(n - 1, 0, -1):
		result **= x
	return result
# print(toExponentFactorial(5))
# Like a factorial but 5 * (4+3+2+1) * 4 * (3+2+1) * 3 * (2 + 1) * 2 * (1) * 1
def toSumWeirdFactorial(n):
	ransum = list(range(n - 1, 0, -1))
	result = n
	for x in range(n - 1, 0, -1):
		result *= sum(ransum)
		del ransum[0]
		result *= x
	return result
print(toWeirdFactorial(6))
