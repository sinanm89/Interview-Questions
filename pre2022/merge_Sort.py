# object App:
#     _id = None
#     _mem_req = None
#     # foreground true, background false
#     _foreground = None

# object Device:
#     _total_mem = None
#     _fore = None
#     _back = None
# #  fore/back preferered, _total_memory >= _memory + _memory
def merge_sort(app_list):
    mid = int(len(app_list)/2)
    if mid <= 1:
        # if list has 2 or 1 elements left (odd/even num of iterables)
        return app_list
    ee = merge(merge_sort(app_list[:mid]), app_list(fore_apps[mid:]))
    print ee
    return ee

def merge(left, right):
    output = []
    # do merge
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l][1] < right[j][1]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
    output += left[l:]
    output += right[r:]
    return output

def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):

    # f/b = [[id_foreground, mem_required],]

    # id_f_mem_map = {"_{k}".format(k=key)=val for key, val in foregroundAppList}
    # id_b_mem_map = {"_{k}".format(k=key)=val for key, val in backgroundAppList}

    # sort by mem required for both
    foregroundAppList = merge_sort(foregroundAppList)

    # starting from both highest and lowest, try to pair up back/fore apps.


