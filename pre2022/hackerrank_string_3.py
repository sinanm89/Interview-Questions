def get_change_num(X):
    X.sort()
    out = {"A":0, "T":0, "G":0, "C":0}
    out_indexes = {"Ai":[], "Ti":[], "Gi":[], "Ci":[]}
    max_gene = None
    for i in range(0, len(X)):
        char = X[i]
        out[char] = out[char] + 1
        key = "{0}i".format(char)
        out_indexes[key].append(i)
        if (
            out['A'] and out['C'] and out['G'] and out['T'] and
            (out['A'] + out['T'] + out['G'] + out['T'])%4 == 0
        ):
            for f in out.keys():
                key = "{0}i".format(f)
                out[f] -= 1
                out_indexes[key].pop()

    # min_changes = 0
    # for k, v in out.items():
    #     min_changes += v%4

    return out_indexes
    # out_count = 0
    # for f in out.keys():
    #     out_count += out[f]
    # return out_count

w1, w2 = "GAAATAAA", "GATC"
print(get_change_num(list(w1)))
