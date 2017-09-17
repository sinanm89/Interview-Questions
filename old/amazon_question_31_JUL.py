        # lookup_price
            lookup_index = i
            for value in input_array[:i]:
                lookup_index -= 1
                if hash_table[value] > lookup_index:
                    delta = bought_price - initial_price


                    if hash_table[value] > lookup_index:
                    delta = bought_price - initial_price





Item bought at index 0
[10, 5, 7, 9, 1, 11]
whats the max_delta for the optimum time?

# precompute step:
# [11, 10, 9, 7, 5, 1]
# {11: 5, 10: 0, 9: 3, 7: 2, 5: 1, 1: 4}
# [(11, 5),(10,0), (9, 3), (7, 2), (5,1), (1,4)]


for price, date in sorted_list:
