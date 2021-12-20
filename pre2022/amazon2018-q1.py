# Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

# For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.

# Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.

# Method 1 (Use Bubble k times)
# Thanks to Shailendra for suggesting this approach.
# 1) Modify Bubble Sort to run the outer loop at most k times.
# 2) Print the last k elements of the array obtained in step 1.

# Time Complexity: O(nk)



# Like Bubble sort, other sorting algorithms like Selection Sort can also be modified to get the k largest elements.

# Method 2 (Use temporary array)
# K largest elements from arr[0..n-1]

# 1) Store the first k elements in a temporary array temp[0..k-1].
# 2) Find the smallest element in temp[], let the smallest element be min.
# 3) For each element x in arr[k] to arr[n-1]
# If x is greater than the min then remove min from temp[] and insert x.
# 4) Print final k elements of temp[]

# Time Complexity: O((n-k)*k). If we want the output sorted then O((n-k)*k + klogk)

# Thanks to nesamani1822 for suggesting this method.

# Method 3(Use Sorting)
# 1) Sort the elements in descending order in O(nLogn)
# 2) Print the first k numbers of the sorted array O(k).
# Following is the implementation of above.


def merge_sort(arr):
    mid = int(len(arr)/2)
    if len(arr) <= 2:
        print(arr)
        if arr[-1] < arr[0]:
            arr[0], arr[-1] = arr[-1], arr[0]
        return arr
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

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

merge_sort([2,5,1,6,4])
