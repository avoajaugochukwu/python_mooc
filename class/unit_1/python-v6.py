#Lecture 5 example without a dictionary
# def keySearch(L, k):
# 	for elem in L:
# 		if elem[0] == k: return elem[1]
# 	return None


# EtoF = {'bread': 'du pain', 'wine': 'du vin', 'eats': 'mange', 'drinks': 'bois', 'likes': 'aime', 1: 'un', '6.00':'6.00'}

# def translateWord(word, dictionary):
# 	if word in dictionary:
# 		return dictionary[word]
# 	else:
# 		return word


# print translateWord('bread', EtoF)


# def translate(sentence):
# 	translation = ''
# 	word = ''
# 	for c in sentence:
# 		if c != ' ':
# 			# print word
# 			word = word + c
# 		else:
# 			translation = translation + ' ' + translateWord(word, EtoF)
# 			word = ''
			# print translation
# 	return translation[1:] + ' ' + translateWord(word, EtoF)
# print translate('John eats bread')
# print translate('Eric drinks wine')
# print translate('Everyone likes 6.00 brea')


# def exp(b, n):
# 	if (n == 0):
# 		return 1
# 	else:
# 		return b * exp(b, n - 1)

# print exp(2, 3)

def toChars(s):
	import string
	s = string.lower(s)
	ans = ''
	for c in s:
		if c in string.lowercase:
			ans = ans + c
	return ans

def isPal(s):
	if len(s) <= 1:
		return True
	else:
		return s[0] == s[-1] and isPal(s[1:-1])


def isPalindrome(s):
	"""Returns true if s is a pallndrome"""
	return isPal(toChars(s))



print isPalindrome('Guttag')
print isPalindrome('Guttug')
print isPalindrome('Able was I ere I saw Elba')
print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')

