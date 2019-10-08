# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        sentinel = ListNode(0)
        sentinel.next = head
        first = sentinel
        second = sentinel
        while second != None:
            if second.next == None:
                first = first.next
                break
            else:
                first = first.next
                second = second.next.next
        return first
