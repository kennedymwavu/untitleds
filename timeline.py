# ----Problem statement----
# Say you're given the following lists of lists representing the activities in the Google calendars of 2 individuals':
p1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
p1_limits = ['09:00', '20:00']

p2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
p2_limits = ['10:00', '18:30']

# p1_limits and p2_limits represent the earliest time the person can have a meeting and the latest time they're
# available

# When can the two people meet during the day?
# Sample output:
# [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

# ----Solution----
# First remove all colons and convert to integers:
# for i in range(len(p1)):
# 	for j in range(len(p1[i])):
# 		p1[i][j] = p1[i][j].replace(":", "")

# print(p1)

# remover fn:
remover = lambda x : int(x.replace(":", ""))

mapper = lambda x : list(map(remover, x))

def rm_colon(given_list):
	"""remove colons from p1 and p2, which are lists of lists"""
	
	# map "mapper" over all elements of given_list:
	mapper2 = lambda x : list(map(mapper, x))

	return mapper2(given_list)

p1 = rm_colon(p1)
p2 = rm_colon(p2)
# print(p1, "\n", p2, sep="")

p1_limits = mapper(p1_limits)
p2_limits = mapper(p2_limits)
# print(p1_limits, "\n", p2_limits, sep="")

