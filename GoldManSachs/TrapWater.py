"""
Leetcode 42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.


Solution:
Base case:
 1 block of any height can't trap water
 2 blocks of any height can't trap water, therefore we need 3 or more heights to trap water
 Note:
 blocks in descending and ascending cannot store any water, so blocks must make a space to store water which means there should left height and right height greater than current height.
Amount of trapped water depends on minimum boundary height--> at any given block trapped water =  min(maxleftheight, maxrightheight) - currentheight

TimeComplexity:

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        trapped Water = min(maxleftheight,maxRightHeight) - currentHeight
        """
        N = len(height)
        leftHeight = [0 for i in range(N)]
        rightHeight = [0 for i in range(N)]
        maxLeft = 0
        maxRight = 0

        for i in range(N):
            if (leftHeight[i] < height[i]) and (height[i] > maxLeft):
                leftHeight[i] = height[i]
                maxLeft = height[i]
            else:
                leftHeight[i] = maxLeft

        for i in range(N - 1, -1, -1):

            if (rightHeight[i] < height[i]) and (maxRight < height[i]):
                rightHeight[i] = height[i]
                maxRight = height[i]
            else:
                rightHeight[i] = maxRight

        totalWater = 0
        for i in range(N):
            totalWater += min(leftHeight[i], rightHeight[i]) - height[i]
        return totalWater





"""
Time complexity: O(n)O(n).
Single iteration of O(n)O(n) in which each bar can be touched at most twice(due to insertion and deletion from stack) and insertion and deletion from stack takes O(1)O(1) time.
Space complexity: O(n)O(n). Stack can take upto O(n)O(n) space in case of stairs-like or flat structure."""
class Solution(object):
    def trap(self, height):

        decreasingHeightIdx = []
        trapWater = 0
        for idx, val in enumerate(height):

            while len(decreasingHeightIdx) > 0 and height[decreasingHeightIdx[-1]] < val:
                previousBottomHeight = height[decreasingHeightIdx.pop()]
                if len(decreasingHeightIdx) == 0:
                    break
                leftHeightIdx = decreasingHeightIdx[-1]
                DiffHeight = min(val, height[leftHeightIdx]) - previousBottomHeight
                width = idx - leftHeightIdx - 1
                trapWater += DiffHeight * width

            decreasingHeightIdx.append(idx)

        return trapWater


obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(obj.trap(height))