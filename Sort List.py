# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        elements=[]
        temp=head
        while temp is not None:
            elements.append(temp.val)
            temp=temp.next
        
        elements=sorted(elements)
        
        temp=ListNode(0)
        curr=temp
        for i in elements:
            curr.next=ListNode(i)
            curr=curr.next
            
        return temp.next
