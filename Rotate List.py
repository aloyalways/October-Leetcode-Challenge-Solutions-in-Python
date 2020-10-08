# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        length=0
        temp=head
        while temp is not None:
            length+=1
            temp=temp.next
        
        if k>=length:
            k=k%length
        if k==0:
            return head
        
        rotate=length-k
        temp=head
        temp_next=head
        prev=head
        while rotate>0:
            prev=temp_next
            temp_next=temp_next.next
            rotate-=1
            
        prev.next=None
        head=temp_next
        while temp_next.next is not None:
            temp_next=temp_next.next
        temp_next.next=temp
        
        return head
