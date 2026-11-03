# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
       
       
        second = prev
        first = head

        while second:
            temp1 = first.next
            first.next = second

            temp2 = second.next
            second.next = temp1

            first = temp1
            second = temp2


        


