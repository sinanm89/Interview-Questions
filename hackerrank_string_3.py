def get_change_num(X):
    X.sort()
    out = {"A":0, "T":0, "G":0, "C":0}
    max_gene = None
    for i in X:
        out[i] = out[i] + 1
        if (
            out['A'] and out['C'] and out['G'] and out['T'] and
            (out['A'] + out['T'] + out['G'] + out['T'])%4 == 0
        ):
            for f in out.keys():
                out[f] -= 1

    min_changes = 0
    for k, v in out.items():
        min_changes += v%4

    return min_changes+1
    # out_count = 0
    # for f in out.keys():
    #     out_count += out[f]
    # return out_count

w1, w2 = "GAAATAAA", "GATC"
print(get_change_num(list(w1)))
