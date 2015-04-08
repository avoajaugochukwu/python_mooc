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

# print checkSex('FeMoney')

hold = []
for i in range(0, 20):
	hold.append(i)
print len(hold)

max_value = max(hold)
min_value = min(hold)

randomized = []
while len(randomized) <= 18:
# for i in hold:
	rand_num = randint(min_value, max_value)
	if rand_num not in randomized:
		randomized.append(rand_num)

print randomized