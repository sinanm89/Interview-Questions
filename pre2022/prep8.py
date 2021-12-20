# harry
# sally
# ay 2


# SHINCHAN
# NOHARAAA
# NHA 3
 

def commonChild(s1, s2):
    max_str_len = 0

    s1_map = {}
    s2_map = {}
    i = 0

    s1_prev_match_index = 0
    s2_prev_match_index = 0

    while i < len(s1) and i < len(s2):
        s1_char = s1[i]
        s2_char = s2[i]

        if s1[i] == s2[i]:
            s1_prev_match_index = i
            s2_prev_match_index = i
            max_str_len += 1
            i += 1
            continue
        else:
            s1_map[s1_char] = s1_map.get(s1_char, []).append(i)
            s2_map[s2_char] = s2_map.get(s2_char, []).append(i)

            if s1_map.get(s2_char):

            elif s2_map.get(s1_char):
                max_str_len += 1
                del s1_map[s2_char]
                del s2_map[s2_char]
            else:
                s1_map[s1_char] = s1_map.get(s1_char, []).append(i)
                s2_map[s2_char] = s2_map.get(s2_char, []).append(i)

            i += 1

    return max_str_len


s1 = 'HARRAY'
s2 = 'AYLHNM'

print(commonChild(s1,s2))
