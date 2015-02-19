class intSet(object):
#An intSet is a set of integers

	def __init__(self):
		"""Create an empty set of integers"""
		self.numBuckets = 47
		self.vals = []
		for i in range(self.numBuckets):
			self.vals.append([])


	def hashE(self, e):
		#Private function, should not be used outside of class
		return abs(e) % len(self.vals)


	def insert(self, e):
		"""Assumes e is an integer and inserts e into self"""
		for i in self.vals[self.hashE(e)]:
			if i == e: return
		self.vals[self.hashE(e)].append(e)


	def member(self, e):
		"""Assumes e is an integer
		Returns True if e is in self, and False otherwise"""
		return e in self.vals[self.hashE(e)]


	def __str__(self): #when you use print it automatically invokes this function
		"""Returns a string representation of self"""
		elems = []
		for bucket in self.vals:
			for e in bucket: elems.append(e)

		elems.sort()
		result = ''
		for e in elems: result = result + str(e) + ','
		return '{' + result[:-1] + '}'


def test1():
	s = intSet()
	for i in range(40):
		s.insert(i)
	print s.member(14)
	print s.member(41)
	print s
# test1()
import datetime


#--------------------------------------------------------



class Person(object):
	import datetime
	def __init__(self, name):
		#create a person with name name
		self.name = name
		try:
			firstBlank = name.rindex(' ')
			self.lastName = name[firstBlank+1:]
		except:
			self.lastName = name

		self.birthday = None


	def getLastName(self):
		#return self's last name
		return self.lastName


	def setBirthday(self, birthDate):
		#assumes birthDate is of type datetime.date 
		 #sets self's birthday to birthDate
		assert type(birthDate) == datetime.date
		self.birthday = birthDate


	def getAge(self):
		#assumes that self's birthday has been set
		#returns self's current age in days
		assert self.birthday != None
		return (datetime.date.today() - self.birthday).days


	def __lt__(self, other):
		#return True if self's name is lexicographically greater
		#than other's name, and False otherwise
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName 

	def __str__(self):
		#return self's name
		return self.name

# me = Person('Avoaja Ugochukwu')
# him = Person('Barack Hussein Obama')
# her = Person('madonna')
# print him
# print him.getLastName()
# him.setBirthday(datetime.date(1961, 8, 9))
# her.setBirthday(datetime.date(1958, 8, 16))
# print him.getAge()
# print her.getAge()
# pList = [me, him, her]
# print 'The people in pList are'
# for p in pList:
# 	print '   ' + str(p)


class MITPerson(Person):  #check this later
	nextIdNum = 0
	def __init__(self, name):
		Person.__init__(self, name)
		MITPerson.nextIdNum += 1
		self.idNum = MITPerson.nextIdNum

	def getIdNum(self):
		return self.idNum

	def __lt__(self, other):
		return self.idNum < other.idNum

	def isStudent(self):
		return type(self) == UG or type(self) == G


ugo = MITPerson('Avoaja')
cha = MITPerson('Charles')
print ugo.getIdNum()
print cha.getIdNum()
print ugo
print cha


class CourseList(object):
	def __init__(self, number):
		self.number = number
		self.students = []

	def addStudent(self, who):
		if not who.isStudent():
			raise TypeError('Not a student')
		if who in self.students:
			raise ValueError('Duplicate student')
		self.students.append(who)

	def remStudent(self, who):
		try:
			self.students.remove(who)
		except:
			print str(who) + ' not in ' + self.number

	def allStudents(self):
		for s in self.students:
			yield s

	def ugs(self):
		indx = 0
		while indx < len(self.students):
			if type(self.students[indx]) == UG:
				yield self.students[indx]
			indx += 1


class UG(MITPerson):
	def __init__(self, name):
		MITPerson.__init__(self, name)
		self.year = None

	def setYear(self, year):
		if year > 5:
			raise OverflowError('Too many')
		self.year = year

	def getYear(self):
		return self.year


class G(MITPerson):
	pass


m1 = MITPerson('barbara Beaver')
ug1 = UG('Jane Doe')
ug2 = UG('John Doe')
g1 = G('Mitch Peabody')
g2 = G('Ryan Jackson')
g3 = G('Sarina Canelake')
SixHundred = CourseList('6.00')
SixHundred.addStudent(ug1)
SixHundred.addStudent(g1)
SixHundred.addStudent(ug2)
print SixHundred.allStudents()
# try:
# 	SixHundred.addStudent(m1)
# except:
# 	print 'Whoops'
# print SixHundred #perhaps not what i expected

SixHundred.remStudent(g3)
print 'students'
for s in  SixHundred.allStudents():
	print s

# print 'students Squared'
# for s in SixHundred.allStudents():
# 	for sl in SixHundred.allStudents():
# 		print s, sl
# print 'Undergraduate'
# for u in SixHundred.ugs():
# 	print u