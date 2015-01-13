# 6.00 Problem Set 3
# 
# Hangman
#
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    # print "Loading word list from file..."
    
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    
    line = inFile.readline()
    
    wordlist = string.split(line)
    # print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):

    return random.choice(wordlist)

#//////////////////////////////////////////////////
#Guessing game
wordlist = load_words()
r_tuple = ()
all_letters = string.lowercase
space = '-'
def stripSting(guess):
    alphabet = guess
    i = 0 #index
    global all_letters
    for n in all_letters:
        if alphabet == all_letters[i]:
            # print all_letters[i]
            all_letters = all_letters.replace(all_letters[i], '_')
            print 'Available letters:', all_letters
        i += 1

def game(guess):
    global r_tuple
    global solution

    if guess in r_tuple[0]:
        i = 0
        for n in r_tuple[0]:
            if guess == r_tuple[0][i]:
                # print i + 1
                solution = list(solution) #change to list
                solution[i] = r_tuple[0][i]
                new_solution = ''.join(solution) #change to string 
                solution = new_solution
                
            i += 1
        print 'You got that right::', solution, '\n'
    else:
        print 'No sir not cool:: ', solution, '\n'


    stripSting(guess)


def hangman():
    global r_tuple
    
    r_word = choose_word(wordlist)
    r_tuple = r_tuple + (r_word,)
    global lenght_random_word
    lenght_random_word = len(r_word)
    global solution
    solution = space *  lenght_random_word

    #---------------------------------------
    print 'Welcome to Hangman game'
    print 'I am thinking of a word that is', lenght_random_word, 'long'
    n_guess_left = lenght_random_word * 2
    #---------------------------------------

    while ( n_guess_left > 0 and solution != r_tuple[0]):
        print '\n'
        print 'you have ', n_guess_left, 'left'
        n_guess_left -= 1
        guess = raw_input('Please guess a letter: ',)
        game(guess)

    print 'guess was :', r_word


hangman()