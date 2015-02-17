import string
def censor(text, word):
    return text.replace(word, "*"*len(word))
# print censor('a', 'bag')

our_string = "this hack is wack hack"

new_str = our_string.replace('hack', '*'*len('hack'))
print (new_str)