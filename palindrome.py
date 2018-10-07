
def find_palindrome(inp):
    char_map = {}
    p_mirror = ''
    out = []
    temp_i = 0

    for i in range(0, len(inp)):
        c = inp[i]
        char_map[c] = char_map.get(c, 0) + 1
        if char_map[c] % 2 == 0:
            m_count = 1
            sp = ''
            for k in range(0, i):
                k = i - k - 1
                if inp[k] != c:
                    if inp[k-m_count] == c:
                        sp = inp[k-m_count:i+1]
                        if len(sp) == 1:
                            break
                        out.append(sp)
                    break
                else:
                    m_count += 1
                    sp = inp[k:i+1]
                    if len(sp) == 1:
                        break
                    out.append(sp)
            char_map[c] = 1

    return out
w1 = 'mnonopoo' # 12
w2 = 'abcbaba' # 10
w3 = 'aaaa' # 10
w4 = 'aabaa' #   aa, aba, aa, aabaa 9
w5 = 'asasd' #   asa sas 7
w6 = 'asaa' #   asa aa 6

# out = find_palindrome(w1)
# print(out, len(out) +  len(w1))

# out = find_palindrome(w2)
# print(out, len(out) +  len(w2))

# out = find_palindrome(w3)
# print(out, len(out) +  len(w3))

# out = find_palindrome(w4)
# print(out, len(out) +  len(w4))

# out = find_palindrome(w5)
# print(out, len(out) +  len(w5))
# import pdb; pdb.set_trace()
# out = find_palindrome(w6)
# print(out, len(out) +  len(w6))

# WORKING WEIRD ASS SOLUTION
# def substrCount(n, s):
#     l = []
#     count = 0
#     cur = None

# # 1st pass
#     for i in range(n):
#         if s[i] == cur:
#             count += 1
#         else:
#             if cur is not None:
#                 l.append((cur, count))
#             cur = s[i]
#             count = 1
#     l.append((cur, count))

#     ans = 0
        
# # 2nd pass
#     for i in l:
#         ans += (i[1] * (i[1] + 1)) // 2

# # 3rd pass
#     for i in range(1, len(l) - 1):
#         if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
#             ans += min(l[i - 1][1], l[i + 1][1])

#     return ans

# print(substrCount(len(w1), w1))
# print(substrCount(len(w2), w2))
# print(substrCount(len(w3), w3))
# print(substrCount(len(w4), w4))
# print(substrCount(len(w6), w6))

# BETTER SOLUTION
# def substrCount(n, s):
#     ret = n
#     i = 1
#     while i < n:
# #First part: find and calculate in substrings that have all same characters
#         l = i
#         r = i
#         while l > 0 and s[l-1] == s[i]:
#             l -= 1
#         while r < n-1 and s[r+1] == s[i]:
#             r += 1        
#         if r - l != 0:
#             size = r - l + 1
#             ret += (size * (size-1)) // 2
#             i = r + 1
#             continue
        
# #Second part: if current character is different than it's both neighbor,
# # see if there is any substring contain special palindrome (where this character is the center of substring)
#         curr = s[i-1]
#         j = 1
#         while i-j >= 0 and i+j < n:
#             if s[i-j] == curr and s[i+j] == curr:
#                 ret += 1
#                 j += 1
#             else:
#                 break
#         i += 1
#     return ret



def special_palindrone(inp):
    out = []
    for curri in range(1, inp-1):
        curr = inp[curri]
        prev = inp[curr-1]
        nexx = inp[curr+1]
        if curr != prev and curr != nexx:
            if prev == nexx:
                out.append(curr[curri-1:curri+2])
