def isPalindrome(word):
	return str(word.lower().replace(",", "").replace(" ", "")) == str(word.lower().replace(",", "").replace(" ", ""))[::-1]
print("Is racecar a palindrome? " + str(isPalindrome("racecar")))
print("Is mom a palindrome? " + str(isPalindrome("mom")))
print("Is a man a plan a canal panama a palindrome? " + str(isPalindrome("a man a plan a canal panama")))
print("Is No x in nixon a palindrome? " + str(isPalindrome("No x in nixon")))
print("Is civic a palindrome? " + str(isPalindrome("civic")))
print("Is Amore, Roma a palindrome? " + str(isPalindrome("Amore, Roma")))
print("Is kayak a palindrome? " + str(isPalindrome("kayak")))
