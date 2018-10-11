def spalin2(n, inp):
    """
    Single pass special palindrome calculator.
    aaabaaa = correct

    aabcbaa = not correct
    """
    out = n
    curr_i = 0
    while curr_i < n:
        factorial_count = 0
        next_i = curr_i + 1
        if next_i >= n:
            break
        if next_i < n and inp[curr_i] == inp[next_i]:
            # strings like aa aaaa fall here
            while next_i < n and inp[curr_i] == inp[next_i]:
                factorial_count += 1
                next_i += 1
            # we already count every single letter on exit
            while factorial_count > 0:
                # aaaa = 4+3+2+1 = 10
                # aaaaa = 5+4+3+2+1 = 15
                out += factorial_count
                factorial_count -= 1
            # import pdb; pdb.set_trace()
            curr_i = next_i
        else:
            prev_i = curr_i - 1
            if prev_i < 0 or prev_i == curr_i:
                curr_i += 1
                continue
            elif (
                prev_i >= 0 and
                inp[prev_i] == inp[next_i] and
                inp[curr_i] != inp[prev_i]
            ):
                # import pdb; pdb.set_trace()
                mirrored_char = inp[next_i]
                while (
                    next_i < n and prev_i >= 0 and
                    inp[prev_i] == inp[next_i] and
                    inp[prev_i] == mirrored_char
                ):
                    # aba aabaa aaabaaa
                    # the lefthand side of the mirrored string is counted
                    out += 1
                    prev_i -= 1
                    next_i += 1
            curr_i += 1
    return out

w1 = 'aabaa' # aa aba aabaa aa + 5 = 9
w2 = 'asasd' # asa sas + 5 = 7
w3 = 'abcbaba' # bcb bab aba + 7
w4 = 'aaaa' # aa aa aa aaa aaa aaaa + 4 = 10
w6 = 'abcccb'
w7 = 'baaacbabbaaabaabbaa' # ee = ["aa", "aa", "aaa", "bab", "bb", "aa", "aa", "aaa", "aba", "aabaa", "aa","bb", "aa"]

print(spalin2(len(w1), w1))

print(spalin2(len(w2),w2))

print(spalin2(len(w3),w3))

print(spalin2(len(w4), w4))
print(spalin2(len(w6), w6))
print(spalin2(len(w7), w7))


with open('input02.txt') as f:
    read_data = f.read()
len_inp = 0
for i in read_data:
    if i == '\n':
        break
    len_inp += 1

w5 = read_data[len_inp+1:]
len_inp = int(read_data[:len_inp])
print(spalin2(len_inp, w5))

# print(substrCount(len_inp, w5))
# print(substrCount(len(w7), w7))
