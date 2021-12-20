def LCSLength(X, Y):
    X = "_" + X
    Y = "_" + Y
    m, k = len(X), len(Y)
    prev = [0 for q in range(0, k)]
    B = [[None for q in range(0, k)] for r in range(0, m)]
    for i in range(1, m):
        temp = [0 for q in range(0, k)]
        for f in range(1, k):
            if X[i] == Y[f]:
                temp[f] = prev[f-1] + 1
                B[i][f] = 1

            elif prev[f] >= temp[f-1]:
                temp[f] = prev[f]
                B[i][f] = 0
            else:
                temp[f] = max(temp[f-1], prev[f])
                B[i][f] = None

        prev = temp
    return temp[-1], B


# w1, w2 = "SHINCHAN", "NOHARAAA"  # 3
# w1,w2 = "GAC","AGCAT"          # 2
w1,w2 = "ABCBDAB","BDCABA"     # 4

print(LCSLength(w1, w2))
