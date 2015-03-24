#A dictionary of critics and their ratings of movies

critics = {
  'Lisa Rose':
    {
      'Lady in the Water': 2.5,
      'Snakes on a plane': 3.5,
      'Just my Luck': 3.0,
      'Superman returns': 3.5,
      'You, Me and Dupree': 2.5,
      'The Night Listener': 3.0
    },
  'Gene Seymour':
    {
      'Lady in the Water': 3.0,
      'Snakes on a plane': 3.5,
      'Just my Luck': 1.5,
      'Superman returns': 5.0,
      'You, Me and Dupree': 3.0,
      'The Night Listener': 3.5
    },
  'Micheal Phillips':
    {
      'Lady in the Water': 2.5,
      'Snakes on a plane': 3.0,
      'Superman returns': 3.5,
      'The Night Listener': 4.0
    },
  'Cluadia Puig':
    {
      'Snakes on a plane': 3.5,
      'Just my Luck': 3.0,
      'Superman returns': 4.0,
      'You, Me and Dupree': 2.5,
      'The Night Listener': 4.5
    },
  'Mick LaSalle':
    {
      'Lady in the Water': 3.0,
      'Snakes on a plane': 4.0,
      'Just my Luck': 2.0,
      'Superman returns': 3.0,
      'You, Me and Dupree': 2.0,
      'The Night Listener': 3.0
    },
  'Jack Matthews':
    {
      'Lady in the Water': 3.0,
      'Snakes on a plane': 4.0,
      'Superman returns': 5.0,
      'You, Me and Dupree': 3.5,
      'The Night Listner': 3.0
    },
  'Toby':
    {
      'Snakes on a plane': 4.5,
      'Superman returns': 4.0,
      'You, Me and Dupree': 1.0,
    },
}
#Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
	# Get the list of shared_items
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	# if they have no common rating, return 0
	if len(si) == 0:
		return 0

	sum_of_squares = 0
	for i in critics[person1]:
		if i in critics[person2]:
			s = critics[person1][i] - critics[person2][i]
			t = pow(s, 2)
			sum_of_squares += t



	return 1 / (1 + sum_of_squares)

for j in critics:
	for k in critics:
		if j != k:
			print j, k
			print sim_distance(critics, j, k)
# print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
# print sim_distance(critics, 'Toby', 'Gene Seymour')
# print sim_distance(critics, 'Toby', 'Micheal Phillips')