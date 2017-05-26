input_list = [1, -2, 3, 6, 1, 0, 6, 6]
#return index of a random max value in the array
max_val = 0
indexes = []
last_found = 0
for i, v in enumerate(input_list):
    if v >= max_val:
        if v == last_found:
            indexes.append(i)
        else:
            indexes = []
        max_val = value

print random.sample(index_table[max_val],1)[0]
