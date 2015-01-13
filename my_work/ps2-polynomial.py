# Problem Set 2:~~
# Name: Avoaja Ugochukwu
# Collaborators: 
# Time Spent: 5:30

# poly = (-6, -5, 2, 1)
#-----------------------------------------
#			polynomials
#polynomials as tuples
#index of tuple represents power, value of index is coefficient


def evaluate_poly(poly, x):		
		length = 0
		answer = 0
		for i in poly:
			if (length < len(poly)):
				_eval = i * (x) ** length
				# print _eval
				length = length + 1
				answer += _eval

		print answer

# poly = (0.0, 0.0, 5.0, 9.3, 7.0)
# evaluate_poly(poly, -13)


#-----------------------------------------
				#Derivative
def compute_deriv(poly):
	length = 0
	answer = 0
	tuples = ()
	for i in poly:
		if (length < len(poly)):			
			power = length - 1
			deri = float(length * i) #+ 'x^' + str(power)
			length = length + 1
			
			if (power >= 0):
				tuples = tuples + (deri,)

	print tuples
    
# poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    
# compute_deriv(poly)


#-----------------------------------------
					#Compute Root Newton-Ralphson
# First, a Derivative formula for f'(x_n)
def compute_deriv_sum(poly, n):
	length = 0; answer = 0; tuples = (); size = 0

	for i in poly:
		if (length < len(poly)):					
			power = length - 1   										#track power of new polynomial to remove 0 and -ve	
			deri = float(length * i) 								#to get values for the tuple: coefficient of new polynomial
			length = length + 1			
			if (power >= 0):
				tuples = tuples + (deri,)

	for t in tuples:
		if (size < len(tuples)):
			_eval = t * ((n) ** size)
			size = size + 1			
			answer += _eval

	# print answer
	return answer #return specific type for more manipulation


n_times = 1
def compute_root(poly, x_0, epsilon):
  length = 0
  fx_0 = 0
  deri_fx_0 = 0
  newton_tuple = ()
  for i in poly:
  	if (length < len(poly)):
  		_eval = i * (x_0) ** length
  		# print _eval
  		length = length + 1
  		fx_0 += _eval
  # print 'fx_0 =', fx_0
  # print 'x_0 =', x_0
  
  if (abs(fx_0) - epsilon >= epsilon):
  	# call f'(x_n):: Derivative
  	deri_v = compute_deriv_sum(poly, x_0)
  	x_1 = x_0 - (fx_0 / deri_v)
  	x_0 = x_1
  	global n_times
  	n_times += 1
  	# print n_times
  	# print  'deri_v', deri_v
  	return compute_root(poly, x_0, 0.0001)
  else:
  	newton_tuple = newton_tuple + (x_0,)
  	newton_tuple = newton_tuple + (n_times,)
  	print newton_tuple

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
compute_root(poly, 0.1, 0.0001)


# poly = (-6, -5, 2, 1) #perfect polynomial where x = -1, 2, -3
# compute_root(poly, 0.1, 0.0001)