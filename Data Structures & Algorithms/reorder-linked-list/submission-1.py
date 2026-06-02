# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s=head
        f=head.next
        while( f and f.next):
            s=s.next
            f=f.next.next

        l2=s.next
        prev=s.next=None
        
        
        while(l2):
            nxt=l2.next
            l2.next=prev
            prev=l2
            l2=nxt
        
        first=head
        second=prev

        while(second):
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
        
        
        

        