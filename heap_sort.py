#         4(0)
#        /   \
#     10(1)   3(2)
#    /   \
# 5(3)    1(4)

#         10(0)
#        /   \
#     5(1)   4(2)
#    /   \
# 3(3)    1(4)

# The numbers in bracket represent the indices in the array
# representation of data.


def heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        print(largest)
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    print('='*90)
    print(arr)
    print('='*90)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

input_array = [4, 10, 3, 5, 1]
out_array = heap_sort(input_array)
print(out_array)
