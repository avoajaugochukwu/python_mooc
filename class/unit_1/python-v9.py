def selSort(L):
	for i in range(len(L) -1):
		minIndx = i
		minVal = L[i]

		j = i + l
		while j < len(L):
			if minVal > L[j]:
				minIndx = j
				minVal = L[j]
			j += 1
		temp L[i]
		L[i] = L[minIndx]
		L[minVal] = temp
		print 'Partialy sorted list =', L