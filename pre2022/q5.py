# There's a room with a TV and people are coming in and out to watch it. The TV is on only when there's at least a person in the room.
# For each person that comes in, we record the start and end time. We want to know for how long the TV has been on. In other words:
# Given a list of arrays of time intervals, write a function that calculates the total amount of time covered by the intervals.
# For example:

# input = [(1,4), (2,3)]
# > 3
# input = [(4,6), (1,2)]
# > 3
# input = {{1,4}, {6,8}, {2,4}, {7,9}, {10, 15}}
# > 11


def find_intervals(in_array):

    input_arr = in_array.sort() # nlogn, now its sorted by the first dimension
    _min = input_arr[0][0]
    _max = input_arr[0][1]
    for i,z in in_array:
        if i > _max:
            _sum += z - i
        if i <= _max:
            _sum += z - i
        if z > _max:
            _max = z
            _sum += z - i
    return _sum

