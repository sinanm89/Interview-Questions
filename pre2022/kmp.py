
def prefixes(txt):
    # txt = "ifailuhkqq" 
    j = 0
    pat = [0]
    for i in range(1, len(txt)):
        if txt[i] == txt[j]:
            j += 1
        else:
            while j > 0 and txt[j] != txt[i]:
                # go back until you find the character that matches
                # the last prefix
                j = pat[j-1]
        pat.append(j)
    return pat

def find_pat(txt="eeeeeifailuhkqq", pat='ifa'):
    partial = prefixes(pat)
    print(partial)
    j = 0
    out = []
    for i in range(0, len(txt)):
        while j > 0 and txt[i] != pat[j]:
            j = partial[j-1]
        if txt[i] == pat[j]:
            j += 1
        if j == len(pat):
            out.append(i-(j-1))
            j = 0
    return out

print(find_pat())
print(find_pat("eeeeeifailuhkqq",'ifai'))

    