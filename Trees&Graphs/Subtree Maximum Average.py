class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

import math
class Solution:
    def maximumAverage(self,root):
        result = [-math.inf, 0]
        avg = 0
        def dfs(root):
            nonlocal avg
            nonlocal result
            if not root:
                return [root.val,1]
            left = dfs(root.left)
            right = dfs(root.right)

            tempSum = root.val + left[0] + right[0]
            count = left[1] + right[1] + 1
            tempAvg = tempSum / count
            if tempAvg > avg:
                avg = tempAvg
                result = [avg, root.val]

            return [tempSum, count]

        dfs(root)
        return result[1]


root = Node(20)
root.left = Node(12)
root.


