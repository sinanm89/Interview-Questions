# Complete the function below.
def merge(left, right):
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out += left[i:]
    out += right[j:]
    return out

def merge_sort(inp):
    mid = len(inp) // 2  # floors int value
    if len(inp) <= 2:
        if inp[-1] < inp[0]:
            inp[0], inp[-1] = inp[-1], inp[0]
        return inp
    return merge(merge_sort(inp[:mid]), merge_sort(inp[mid:]))
    
def jobOffers(scores, lowerLimits, upperLimits):

    low_range = len(lowerLimits)
    high_range = len(upperLimits)
    if low_range != high_range:
        raise Exception('limit length does not match.')
    
    scores = merge_sort(scores)
    # scores.sort() works as well at nlogn time (timsort)
    
    min_lookup_i, max_lookup_i = 0, 0
    out_min, out_max = [], []
    for i in range(0, len(scores)):
        if lowerLimits and scores[i] >= lowerLimits[0] and scores[i] <= upperLimits[0]:
            out_min.append(scores[i])
        if upperLimits and scores[i] >= upperLimits[-1] and scores[i] <= lowerLimits[-1]:
            out_max.append(scores[i])
    
    if low_range >= 1 and high_range >= 1:
        return [len(out_min), len(out_max)]
    elif low_range >= 1:
        return len(out_min)
    else:
        return len(out_max)