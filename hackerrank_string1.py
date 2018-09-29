
def find_common(w1, w2):
	t_w1, t_w2 = list(w1), list(w2)

	t_w1.sort()
	t_w2.sort()

	i, j = 0, 0
	oi1, oi2 = [], []
	while i < len(w1) and j < len(w2):
		if t_w1[i] == t_w2[j]:
			# import pdb; pdb.set_trace()
			out.append(t_w1[i])
			# oi1.append(w1.index(t_w1[i]))
			# oi2.append(w2.index(t_w2[j]))
			i += 1
			j += 1
		elif t_w1[i] < t_w2[j]:
			i += 1
		elif t_w1[i] > t_w2[j]:
			j += 1

	for i in out:
		oi1.append(w1.index(i))
		oi2.append(w2.index(i))

	return find_longest_common_piece(w1, w2, oi1, oi2)

def find_longest_common_piece(w1, w2, oi1, oi2):
	out = []
	oi1.sort()
	oi2.sort()
	# print(oi1, oi2)
	i, k = 0, 0
	import pdb; pdb.set_trace()
	while oi1 and oi2:
		l1_i = oi1.pop(-1)
		l2_i = oi2.pop(-1)
		# print(w1[l1_i], w2[l2_i])
		if w1[l1_i] != w2[l2_i]: 
			continue
		else:
			out.append(w1[l1_i])

	return leout

w1, w2 = 'harry', 'sally'
o = find_common(w1,w2)
print(len(o))

w1, w2 = 'AA', 'BB'
o = find_common(w1,w2)
print(len(o))

w1, w2 = 'ABCDEF', 'FBDAMN'
o = find_common(w1,w2)
print(len(o))

w1, w2 = 'SHINCHAN', 'NOHARAA'
o = find_common(w1,w2)
print(len(o))
