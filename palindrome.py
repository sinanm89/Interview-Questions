def find_palindrome(inp):
    char_map = {}
    p_mirror = ''
    out = []
    temp_i = 0
    for i in range(0, len(inp)):
        c = inp[i]
        char_map[c] = char_map.get(c, 0) + 1
        if char_map[c] % 2 == 0:
            print('start at', i, char_map,inp[i], inp[:i+1])
            m_count = 1
            sp = ''
            if i == 1:
                sp = inp[:i+1]
            elif i == len(inp)-1:
                sp = inp[i-1:]
                # out.append(sp)
            for k in range(i-1, 0, -1):
                if inp[k] != c:
                    if inp[k-m_count] == c:
                        sp = inp[k-m_count:i+1]
                        break
                    else:
                        break
                # elif k - m_count < 0:
                    # break
                else:
                    m_count += 1
                    sp = inp[k:i+1]
            if sp != '':
                out.append(sp)
            char_map[c] = 1

    return out
w1 = 'mnonopoo'
# w1 = 'abcbaba' # 
# w1 = 'aaaa' # 10
w1 = 'aabaa' # aa, aba, aa, aabaa 9
out = find_palindrome(w1)
print(out)
print(out, len(out) +  len(w1))