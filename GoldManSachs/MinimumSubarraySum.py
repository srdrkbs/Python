"""
209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

nums = [2,3,1,2,4,3]

t = 7
sum(nums[i]) == t
return len(nums)
if nums[i:j] < t
 j += 1
if nums[i:j] > t
i+= 1
j = i+1


"""
class Solution:
    def minSubArrayLen(self, target,nums):  #using two pointer approach
        start, end = 0,0
        N = len(nums)
        minLen =  N+1
        temp = 0
        while end < N:
            while temp < target and end < N:
                temp += nums[end]
                end += 1
            while temp >= target and start < N:
                if end - start < minLen:
                    minLen = end - start
                temp -= nums[start]
                start+=1
        return 0 if minLen == N + 1 else minLen


obj = Solution()
# nums = [2, 3, 1, 2, 4, 3]
# target = 7
# nums = [1,4,4]
# target = 4
# target = 11
# nums = [1,1,1,1,1,1,1,1]
target = 11
nums = [1,2,3,4,5]
print(obj.minSubArrayLen(target,nums))


