n = 7
ar = [1,2,1,2,1,3,2]


def sockMerchant(n, ar):
    f_map = {}
    pairs = 0
    for i in ar:
        if f_map.get(i) and f_map.get(i) > 0:
            f_map[i] = f_map[i] + 1
            if f_map[i] % 2 == 0:
                pairs += 1
        else:
            f_map[i] = 1
    return pairs

num_pairs = sockMerchant(n, ar)
print(num_pairs)
