# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode <{self.val}>'

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None:
            return None
        
        i = 0
        _after = None
        _before = head
        origin = head
        
        while 1:
            
            new_node = head.next
           
            if new_node:
                if i == n - 1:
                    _before = head
                    _after = head.next
                    # so next value will also set the nth from last one
                i += 1
                head = head.next
            else:
                _before.next = _after.next
                return origin


def print_ll(origin):
    out = []
    while origin:
        out.append(origin.val)
        origin = origin.next
    print(f'result========== {out}')


def make_ll(head):

    _next = ListNode(val=head[-1])
    head = head[:-1]
    for count, val in enumerate(head[::-1]):
        _next = ListNode(val=val, next=_next)
    print_ll(_next)
    return _next



head = [1,2,3,4,5]
n = 2

ret = Solution().removeNthFromEnd(make_ll(head), n)
print_ll(ret)

head = [1]
n = 1

ret = Solution().removeNthFromEnd(make_ll(head), n)
print_ll(ret)

head = [1,2]
n = 1

ret = Solution().removeNthFromEnd(make_ll(head), n)
print_ll(ret)

head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
n = len(head) - 1


ret = Solution().removeNthFromEnd(make_ll(head), n)
print_ll(ret)


head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
n = len(head) - 2

ret = Solution().removeNthFromEnd(make_ll(head), n)
print_ll(ret)
