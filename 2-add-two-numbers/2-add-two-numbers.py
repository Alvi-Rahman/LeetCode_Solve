# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def lst2link(self, lst):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        _sum = ""
        while l1 is not None or l2 is not None:
            i = (l1.val if l1 is not None else 0) 
            j = (l2.val if l2 is not None else 0)
            carry = i + j + carry
            _sum += str(carry % 10)
            carry = int(carry/10)

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry:
            _sum += str(carry)

        return self.lst2link([i for i in _sum])