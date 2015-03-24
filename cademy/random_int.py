from random import randint
import datetime

# print random.randint(0, 5)

# print datetime.datetime.today().year
# print datetime.datetime.today().month
# print datetime.datetime.today().day


def mainOrderId():
	orderId = ''
	orderId += str(datetime.datetime.today().year)
	orderId = orderId[2:]
	orderId += '0'
	orderId += str(datetime.datetime.today().month)
	orderId += str(datetime.datetime.today().day)

	for i in range(0, 4):
		orderId += str(randint(0, 9))

	orderId = 'T' + orderId
	return orderId