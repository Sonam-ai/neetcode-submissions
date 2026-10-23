# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        dummy=ListNode(0,head)
        prev=dummy
        
        for _ in range(length-n):
            prev=prev.next

        prev.next=prev.next.next

        return dummy.next



        