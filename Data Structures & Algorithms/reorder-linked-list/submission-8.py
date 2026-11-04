# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next = None
        prev = None
        cur = sec

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        sec = prev
        first = head

        while sec:
            temp1, temp2 = first.next, sec.next
            first.next = sec
            sec.next = temp1
            first, sec = temp1, temp2
        
        