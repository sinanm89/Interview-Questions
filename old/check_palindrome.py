shorter_array = [1, 4, 10, 30]

longer_array = [0, 2, 4, 5, 9]

output = [0 for c in xrange(0,len(longer_array) + len(shorter_array))]

while i < len(shorter_array):
    if shorter_array[i] >= longer_array[-1]:
        output.append(shorter_array[i])
        output += longer_array[i:]
        break
    elif longer_array[i] >= shorter_array[-1]:
        output.append(longer_array[i])
        output += shorter_array[i:]
        break

    # get length away from midpoint
    # get indexed values of the 2 mirroring elements in the array
    # check to see if either is larger or smaller than each other
    # append
    # repeat
