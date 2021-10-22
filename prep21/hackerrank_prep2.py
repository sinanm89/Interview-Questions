import math

n = 882787
ar = 'aab'

def repeatedString(s, n):

    if len(s) == n:
        return 1

    modulus_list = []
    for i, character in enumerate(s):
        if character == 'a':
            modulus_list.append(i)
    if len(modulus_list) == 0:
        return 0

    amount_in_str = len(modulus_list)
    amount_in_pattern = math.floor(n / len(s)) * amount_in_str
    amount_in_remaining = (n % len(s)) - 1

    for mod_item in modulus_list:
        if amount_in_remaining == mod_item:
            amount_in_pattern += 1
            break
        elif mod_item <= amount_in_remaining:
            amount_in_pattern += 1

    return amount_in_pattern


num_pairs = repeatedString(ar, n)
print(num_pairs)
