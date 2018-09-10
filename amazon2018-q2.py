# write a program such that it finds the following pythogorean triplet
# inside a given array
#                        (c^2+b^2) - a^2 = 0
#
# arr = [3, 1, 4, 6, 5]
# inp = [3, 8, 7, 4 ,5 ,2 ,11, 9, 10]

def merge(left, right):
    output, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output += left[i:]
    output += right[j:]
    return output

def merge_sort(arr):
    mid = int(len(arr)/2)
    if mid <= 1:
        if arr[1] < arr[0]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def calc(out):
    for i in out:
        j = 0
        k = len(out) - 1
        while j < k:
            if out[j] + out[k] - i == 0:
                print ("{0} + {1} = {2}".format(out[j] , out[k], i))
                print('TRUUUUUUUEEEEEEEE')
                break
            else:
                if out[j] + out[k] < i:
                    j += 1
                else:
                    k -= 1

inp = [3, 8, 7, 4, 5, 2, 11, 9, 10]
out = []
for i in range(0, len(inp)):
    out.append(inp[i] * inp[i])

out = merge_sort(out)
calc(out)
