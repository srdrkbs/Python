"""
What are qualities of a palindrome string? It has even number counts of characters or at most just one character with an odd count.
This means the string is either of even length or an odd length with just exactly one character with an odd count.

266. Palindrome Permutation
Given a string s, return true if a permutation of the string could form a palindrome
Input: s = "aab"
Output: true
Input: s = "code"
Output: false

"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freqCount = {}
        for char in s:   #character count in string
            if char in freqCount:
                freqCount[char] += 1
            else:
                freqCount[char] = 1
        countOdd = 0
        for key, val in freqCount.items():
            if val % 2 != 0:    # if a character count is odd then increement countOdd
                countOdd += 1
        N = len(s)
        if N % 2 == 0:
            return countOdd == 0  # if length is even and no character count is odd then return True
        else:
            return countOdd == 1  # if length is odd and it has exactly one character with odd count then eturn True

obj = Solution()
print(obj.canPermutePalindrome('aab'))