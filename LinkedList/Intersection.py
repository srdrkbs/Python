"""
Leetcode 160. Intersection of Two Linked Lists

"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def insert(val):
    new_val = ListNode(val)
    new_val.val =  val
    new_val.next = None
    return new_val

#using hash map, time complexity: O(NA + NB)
    def getIntersectionNode(self, headA, headB):
        nodesA = set()
        while headA:
            nodesA.add(headA)
            headA = headA.next

        while headB:
            if headB in nodesA:
                return headB
            headB = headB.next

        return None

# using two pointers, time complexity: O(NA +NB)
    def getIntersectionNode(self, headA, headB):
        pointA = headA
        pointB = headB

        while pointA != pointB:
            pointA = headB if pointA is None else pointA.next
            pointB = headA if pointB is None else pointB.next

        return pointA






l1 = insert(4)
l1.next = insert(1)
l1.next.next = insert(8)
l1.next.next.next = insert(4)
l1.next.next.next.next = insert(5)

l2 = insert(5)
l2.next = insert(0)
l2.next.next = insert(1)
l2.next.next.next = insert(8)
l2.next.next.next.next = insert(4)
l2.next.next.next.next.next = insert(5)

res = getIntersectionNode(l1,l2)
print(res)