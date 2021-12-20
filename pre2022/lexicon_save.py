#
# Complete the 'calculateScore' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING text
#  2. STRING prefixString
#  3. STRING suffixString
#
def find_common_characters(t1, t2):
    t1 = list(t1)
    t1.sort()
    t2 = list(t2)
    t2.sort()
    out, i, k = [], 0, 0 
    while i < len(t1) and k < len(t2):
        if t1[i] > t2[k]:
            k += 1
        elif t2[k] > t1[i]:
            i += 1
        elif t2[k] == t1[i]:
            out.append(t1[i])
            i += 1
            k += 1
    return out

def find_longest_substring(t1, t2, commons):
    substring = []
    t2 = t2[::-1]
    # engine
    # e
    # nevar
    #  e
    for i in range(0, len(t1)):
        if t1[i] not in commons:
            continue
        for k in range(0,len(t2)):
            if t1[i] == t2[k]:
                while t1[i] == t2[k]:
                    substring.append(t1[i])
                    i+=1
                    k-=1
                    if i >= len(t1) or k < 0:
                        return substring
    return substring


def find_longest_substring2(t1, t2, commons):
    substring = []
    t1 = t1[::-1]
    for i in range(0, len(t1)):
        if t1[i] not in commons:
            continue
        for k in range(0,len(t2)):
            if t1[i] == t2[k]:
                while t1[i] == t2[k]:
                    substring.append(t1[i])
                    i+=1
                    k+=1
                    if i >= len(t1) or k >= len(t2) or len(substring)*2 >= len(t2):
                        return substring
    return substring

def get_lexicon_order(t1, t2):
    if t1[0] < t2[0]:
        return t1
    else:
        i, j = 0, 0
        while t1 and t2:
            if t1[0] == t2[0]:
                i+=1
                j+=1 
            if t1[0] > t2[0]:
                return t2
            else:
                return t1
            
def calculateScore(text, prefixString, suffixString):
    # Write your code here
#     find common characters in both text|prefix text|suffix
    p_common = find_common_characters(text, prefixString)
#     starting from the beginning find the longest substring
    p_sub = find_longest_substring(text, prefixString, p_common)
    s_common = find_common_characters(text, suffixString)
    print(p_sub)
    s_sub = find_longest_substring2(text, suffixString, s_common)
    print(s_sub)


    if len(s_sub) > len(p_sub):
        return suffixString
    elif len(s_sub) < len(p_sub):
        return prefixString
    if len(s_sub) == len(p_sub):
        return get_lexicon_order(suffixString, prefixString)
        
print(calculateScore('engine','raven', 'ginko'))
print(calculateScore('ab','a', 'b'))