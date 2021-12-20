
def create_letter_factorial_map(w1):

	word_map = {}

	for index, letter in enumerate(w1):
		j_factorial = index + 1
		while j_factorial <= len(w1):
			letter_factorial = w1[index:j_factorial]

			letters_index_array = [[index, j_factorial]]
			if word_map.get(letter) is None:
				word_map[letter] = { letter_factorial : letters_index_array }
			else:
				if word_map[letter].get(letter_factorial):
					word_map[letter][letter_factorial] += letters_index_array
				else:
					word_map[letter][letter_factorial] = letters_index_array
			j_factorial += 1

	print(word_map)
	return word_map

def get_max_len(w1_letter_map, w2_letter_map):
	max_len = 0
	for i in word_map_indexes:
		if letter == i:
			max_len += 1

	return max_len
 # 'y': {'y': [[4, 5]]}}
 # [from, to]
w1, w2 = 'harry', 'sally'

w1_map = create_letter_factorial_map(w1)
w2_map = create_letter_factorial_map(w2)



w1_letters = w1_map.keys()
w2_letters = w2_map.keys()

if len(w1_letters) < len(w2_letters):

	for i in w1_letters:
		if w2_map.get(i):
			get_max_len(w1_map.get(i), w2_map.get(i))

else:

print(len(o))

# w1, w2 = 'AA', 'BB'
# o = find_common(w1,w2)
# print(len(o))

# w1, w2 = 'ABCDEF', 'FBDAMN'
# o = find_common(w1,w2)
# print(len(o))

# w1, w2 = 'SHINCHAN', 'NOHARAA'
# o = find_common(w1,w2)
# # print(len(o))


# ha
# har
# harr
# harry

# a
# ar
# arr
# arry

# r
# rr
# rry

# ry
