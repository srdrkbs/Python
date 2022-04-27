class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self,root):
        def check(root,low=float('-inf'),high=float('inf')):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return check(root.left,low,root.val) and check(root.right,root.val,high)
        return check(root)


root = Node(5, Node(1), Node(4,Node(3),Node(6)))


# root.left = Node(1)
# root.right = Node(4)
obj = Solution()
print(obj.isValidBST(root))
