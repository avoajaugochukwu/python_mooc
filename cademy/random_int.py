from random import randint
import datetime

# print random.randint(0, 5)

# print datetime.datetime.today().year
# print datetime.datetime.today().month
# print datetime.datetime.today().day


def checkSex(word):
	cut = word[:1]
	if cut == 'M':
		return 'M'
	else:
		return 'F'

print checkSex('FeMoney')