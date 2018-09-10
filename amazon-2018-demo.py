# both neighbors active or inactive => cell is inactive next day
# otherwise active next day

# [1, 0, 0, 0, 0, 1, 0, 0], 1
# [0, 1, 0, 0, 1, 0, 1, 0], 0

# [1, 1, 1, 0, 1, 1, 1, 1], 2
# [1, 0, 1, 0, 1, 0, 0, 1], 1
# [0, 0, 0, 0, 0, 1, 1, 0], 0


def cellCompete(states, days):
    for i in range(0, days):
        next_states = []
        j = len(states) - 1
        for i in range(0, j+1):
            # handle first and last element state checks
            _prev = 0 if i == 0 else states[i-1]
            _next = 0 if i == j else states[i+1]
            # check if current state is active or not
            if _next == _prev:
                # invalidate
                next_states.append(0)
            else:
                # otherwise valid
                next_states.append(1)
        states = next_states
    return states

#cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1)
# cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2)

# %100 complete

================================================
Greatest common divisor , Highest common factor, largest pos int that div num

arr = [2342, 2323 ,233 ]
# num =5 #number of items inside array
# arr = 2 4 6 8 10 #array of positive integers
# out: 2 #GCD
# ----
# 5
# 2 3 4 5 6
# 1


# 5
# 2 4 6 8 10
# 2

# arr = [2, 4, 6, 8, 10]
# arr = [3, 6, 9, 12]

arr = [0, -10, 10, 100]

def generalizedGCD(num, arr):
    arr.sort(reverse=True)
    # merge sort in ascending order, smallest item first, complexity nlogn
    pivot = 1
    while arr:
        # set temporary pivot
        _pivot = arr.pop()
        if _pivot <= 0:
            raise Exception('Must be positive integers.')
        for i in arr:
            if i % _pivot != 0:
                # return last known GCD
                return pivot
        # set the current pivot to the verified GCD
        pivot = _pivot
    return pivot

# 6/13 COMPLETE
