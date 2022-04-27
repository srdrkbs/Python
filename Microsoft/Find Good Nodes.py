"""
Leetcode 1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""


class Solution(object):
    def goodNodes(self, root):  #with recursion O(n) n -number of nodes
        def findGoodNodes(root,maxVal):
            if not root: return
            maxVal = max(maxVal,root.val)

            leftGoodCount = findGoodNodes(root.left, maxVal) if root.left else 0
            rightGoodCount = findGoodNodes(root.right,maxVal) if root.right else 0
            return leftGoodCount + rightGoodCount + (root.val>= maxVal)
        return findGoodNodes(root,root.val)

    def goodNodes(self, root): #using DFS O(n)
        if not root: return 0
        stack = [(root, root.val)]
        maxList = []
        while stack:
            node, maxVal = stack.pop()
            if node.val >= maxVal:
                maxList.append(node.val)

            if node.left:
                stack.append((node.left, max(node.left.val, maxVal)))

            if node.right:
                stack.append((node.right, max(node.right.val, maxVal)))

        return len(maxList)
