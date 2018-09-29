def LCSLength(X, Y):
    m, k = len(X), len(Y)
    C = [[0 for q in range(0, k)] for r in range(0, m)]
    B = [['-' for q in range(0, k)] for r in range(0, m)]
    for i in range(1, m):
        for f in range(1, k):
            if X[i] == Y[f]:
                # try:
                C[i][f] = C[i-1][f-1] + 1
                B[i][f] = u'\u2196'
                # except:
                    # import pdb; pdb.set_trace()
            elif C[i-1][f] >= C[i][f-1]:
                C[i][f] = C[i-1][f]
                B[i][f] = u'\u2191'

            else:
                C[i][f] = max(C[i][f-1], C[i-1][f])
                B[i][f] = '-'
    return C, B


def backtrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return {""}
    if X[i] == Y[j]:
        return {Z + X[i] for Z in backtrackAll(C, X, Y, i-1, j-1)}
    R = {""}
    if C[i][j-1] >= C[i-1][j]:
        # import pdb; pdb.set_trace()
        R = R.union(backtrackAll(C, X, Y, i, j-1))
    if C[i-1][j] >= C[i][j-1]:
        # import pdb; pdb.set_trace()
        R = R.union(backtrackAll(C, X, Y, i-1, j))
    return R

# match the longest common string in the given strings.
w1, w2 = list("ABCDEFG"), list("BCDGK")
# MJAU
w1, w2 = "XMJYAUZ", "MZJAWXU"
# w1, w2 = "SHINCHAN", "NOHARAAA"

w1,w2 = "GAC","AGCAT"
w1,w2 = "_ABCBDAB","-BDCABA"
C, B = LCSLength(w1, w2)
for i in range(len(C)): print(C[i], "\t", B[i]) 
print('-'*30)

print(backtrackAll(C, w1, w2, len(w1)-1, len(w2)-1))
