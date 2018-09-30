def optimised_LCSLength(X, Y):
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

# def backtrackAll(C, X, Y, i, j):
#     if i == 0 or j == 0:
#         return {""}
#     if X[i] == Y[j]:
#         return {Z + X[i] for Z in backtrackAll(C, X, Y, i-1, j-1)}
#     R = {""}
#     if C[i][j-1] >= C[i-1][j]:
#         # import pdb; pdb.set_trace()
#         R = R.union(backtrackAll(C, X, Y, i, j-1))
#     if C[i-1][j] >= C[i][j-1]:
#         # import pdb; pdb.set_trace()
#         R = R.union(backtrackAll(C, X, Y, i-1, j))
#     return R

def backtrackLCS(word, solution_t, x, y):
    if x == 0 or y == 0:
        return 
    if solution_t[x][y] == 'd':
        backtrackLCS(word, solution_t, x-1, y-1)
        # print(word[y-1]) # w2
        print(word[x-1]) # w1
    elif solution_t[x][y] == 'u':
        backtrackLCS(word, solution_t, x-1, y)
    else:
        backtrackLCS(word, solution_t, x, y-1)

# match the longest common string in the given strings by taking
# out 0 or more elements from either string
w1, w2 = list("ABCDEFG"), list("BCDGK")
# MJAU
w1, w2 = "XMJYAUZ", "MZJAWXU"
w1, w2 = "SHINCHAN", "NOHARAAA"
# w1,w2 = "GAC","AGCAT"
# w1,w2 = "ABCBDAB","BDCABA"
max_len, solution = optimised_LCSLength(w1,w2)
for i in range(len(C)): print(C[i], "\t", B[i])
print('-'*30)
# print(backtrackAll(C, w1, w2, len(w1)-1, len(w2)-1))
import pdb; pdb.set_trace()
backtrackLCS(w1, solution, len(solution)-1, len(solution[0])-1)