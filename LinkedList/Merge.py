# Leetcode: Merge Two Lists
class ListNode:

    def __init__(self,x):
        self.val = x
        self.next = None


class Merge:
    def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> ListNode:
        temp = None
        # If any of the two lists are empty then return the other one
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next, l2)
        else:
            temp = l2
            temp.next = self.mergeTwoLists(l1,l2.next)
        return temp

    #iterative approach
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)
        first = result
        while l1 and l2:
            if l1.val <= l2.val:
                first.next = ListNode(l1.val)
                l1 = l1.next
            else:
                first.next = ListNode(l2.val)
                l2 = l2.next
            first = first.next
        first.next = l1 if l1 is not None else l2

        return result.next