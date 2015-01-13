import random
import string
WORDLIST_FILENAME = "words.txt"
def load_words():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist
def choose_word(wordlist):
    return random.choice(wordlist)
#-----------------------------------------
wordlist = load_words()
letters = string.lowercase
random_word = choose_word(wordlist)
length_of_word = len(random_word)
working = '-' * length_of_word
working = list(working)
num_guesses = 8
wrong_choices = []

def printOut(value = ''):
		if value == 'correct':
			print "Great choice, you got that right"
		elif value == 'wrong':
			print "Nope bad choice try again"
		elif value == 'num':
			print "number of guess left", num_guesses
		else:
			print 'You have chosen this word before'

#check if gues is in random word
def checkGuess(guess):
	if guess in random_word:
		return True
	return False

"""		1. get index of correct char in random_word
	 		2. explode random_word to list to test its individual values
	 		3. replace "-" with "guess" for [i] """
def fillGuess(guess):  #guess is right, enter guess in final answer
	index = random_word.index(guess)
	random_word_list = list(random_word)
	for i in range(length_of_word):
		if guess == random_word_list[i]:
			working[i] = guess 
			new_working = ''.join(working)
	print "Available letters", new_working

def unusedLetters(guess): #shows unused letters in the alphabet
	global letters
	for i in range(25):
		if guess == letters[i]:
			letters = letters.replace(letters[i], '_')
			print letters

				#Start Game
#----------------------------#
print "I am thinking of a word that is", length_of_word, random_word
printOut('num')

while working != random_word and num_guesses > 0:
	guess = str(raw_input('\n\nEnter a letter', ))
	check = checkGuess(guess) #call checkGuess function
	if check == True: 
		if guess not in working: # check if guess has been chosen before
			fillGuess(guess)
			unusedLetters(guess)
		printOut('correct')
		printOut('num')
	#-----------------------------------------
	else:
		printOut('wrong')
		if guess  in wrong_choices:
			printOut() #prints you have chosen this word before
			printOut('num')
		#-----------------------
		else:
			num_guesses -= 1
			printOut('num')
			if num_guesses == 2:
				print "Warning! final attemp"
		wrong_choices += (guess,)