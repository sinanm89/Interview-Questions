# merge 2 sorted lists.
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]


# 5 , 27
def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    i1 = 0
    i2 = 0
    output = []
    while i1 < len(l1) and i2 < len(l2):
        l1_item = l1[i1]
        l2_item = l2[i2]

        while l1_item < l2_item:
            i1 += 1
            l1_item = l1[i1]
            output.append(l1_item)

        while l2_item < l1_item:
            i2 += 1
            l2_item = l2[i2]
            output.append(l2_item)

        if l2_item == l1_item:
            output.append(l1_item)
            output.append(l2_item)
            i1 += 1
            i2 += 1
    return output
