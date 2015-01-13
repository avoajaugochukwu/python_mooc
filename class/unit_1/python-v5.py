# Techs = ['MIT', 'Cal Tech', 2]
# Ivys =  ['Harvard', 'Yale', 'Brown']
# Univs = []
# Univs.append(Techs)
# print 'Univs = ', Univs

# Univs.append(Ivys)
# print 'Univs =', Univs
# for e in Univs:
# 	print 'e =', e
# flat = Techs + Ivys

# art = ['REID', 'Harvard']
# for u2 in art:
# 	if u2 in flat:
# 		flat.remove(u2)

# flat.sort()
# print 'flat =', flat

# flat[1] = 'UMass'
# print 'flat =', flat

# print 'flat =', flat

# print flat
# def copyList(LSource, LDest):
# 	for e in LSource:
# 		LDest.append(e)
# 		print 'Dest =', LDest

# L1 = [2]
# L2 = [L1, L1]
# print 'L2 = ', L2
# L1[0] = 3
# print 'L2 =', L2
# L2[0] = 'a'
# print 'L2 =', L2

# L1 = [2]
# L2 = L1
# L2[0] = 'a'
# print 'L1 =', L1
# print 'L2 =', L2

# LD = []
# LS = [1, 2, 3]
# copyList(LS, LD)
# print LD
# print LS 

# Dictionary
# D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
# D1 = D
# print D1
# D[1] = 'uno'
# print D1
# D['pi'] = 'I dont know'
# print D1
# for k in D1.keys():
# 	print k, '=', D1[k]


EtoF = {'bread': 'du pain',
				 'wine': 'du vin',
				 'eats': 'mange', 
				 'drinks': 'bois',
				  'likes': 'aime',
				   1: 'un',
				    '6.00':'6.00'}
# print EtoF
# print EtoF.keys() 
# print EtoF.keys
# del EtoF[1]
# print EtoF

#Dicts translation

def translateWord(word, dictionary):
	if word in dictionary:
		return dictionary[word]
	else:
		return word

def translate(sentence):
	translation = ''
	word = ''
	for c in sentence:
		if c != ' ':
			word = word + c
		else:
			translation = translation + ' ' + translateWord(word, EtoF)
			word = ''
	return translation[1:] + ' ' + translateWord(word, EtoF)
print translate('John eats bread')
print translate('Steve drinks wine')
print translate('John likes 6.00')



# def keySearch(L, k):
# 	for elem in L:
# 		if elem[0] == k: return elem[1]
# 	return None
