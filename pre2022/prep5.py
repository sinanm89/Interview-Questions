# ee = [12,1,10,50,5,15,45]
# ee = [2,3,5,1,7,4,4,4,2,6,0]
# [12, 1, 10, 50, 5, 15, 45]
# [1, 5, 10, 12, 15, 45, 50]

print(ee)


def merge_sort(inp_arr: [int]):
    arr_half = int(len(inp_arr)/2)

    if len(inp_arr) < 2:
        return inp_arr

    first_half = merge_sort(inp_arr[:arr_half])
    second_half = merge_sort(inp_arr[arr_half:])

    i = 0
    j = 0
    out = []

    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            out.append(first_half[i])
            i += 1
        elif first_half[i] > second_half[j]:
            out.append(second_half[j])
            j += 1
        elif first_half[i] == second_half[j]:
            out += [first_half[i], second_half[j]]
            i += 1
            j += 1

    if i == len(first_half):
        out += second_half[j:]
    elif j == len(second_half):
        out += first_half[i:]
    
    return out


print(merge_sort(ee))
