def isAnagram(in1, in2):
	# If the length of the first string is not equal to the length of the second string
	# It is obviously not an anagram
	if (len(in1.replace(" ", "")) is not len(in2.replace(" ", ""))):
		return False
	# If the sorted list of the letters in the first string is equal to the second
	# Then it is an anagram
	return sorted(in1.replace(" ", "").lower()) == sorted(in2.replace(" ", "").lower())
print(isAnagram("anagram", "nag a ram"))
