"""
Leetcode 1636. Sort Array by Increasing Frequency
Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

"""

def frequencySort(nums):
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    sortedNums = sorted(nums,reverse = True)
    return sorted(sortedNums, key=lambda x:count[x])

nums = [1,1,2,2,2,3]
print(frequencySort(nums))