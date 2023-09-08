# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getListLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        listA = getListLength(headA)
        listB = getListLength(headB)

        while listA > listB:
            listA -= 1
            headA = headA.next

        while listB > listA:
            listB -= 1
            headB = headB.next

        
        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

