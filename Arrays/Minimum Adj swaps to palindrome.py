"""
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.

Time  : O(N^2)
Space : O(N), where N = len(s)
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
            return countOdd == 1

    def min_swaps(self,s):  #using two pointers
        if not self.canPermutePalindrome(s):
            return -1
        s = list(s)  #since string is immutable converting to list
        front,back = 0, len(s)-1   #two pointers
        minSwap = 0
        while front < back:  # --> two cases will check
            if s[front] == s[back]:  # CASE 1: if front and back char are equal
                front += 1
                back -= 1
            else:  # CASE 2: front != back

                # finding the rightmost character that matches the front char --> we will two cases here
                mid = back
                while s[mid] != s[front] and mid > front:
                    mid -= 1

                if mid == front:  # case 1: if char not found--> swap once with right neighbor and continue the while loop
                    s[mid], s[mid+1] = s[mid+1], s[mid]
                    minSwap += 1
                    continue

                for i in range(mid,back):  #case 2: if char found --> SWAP WITH RIGHT NEIGHBOR UNTIL IT ENDS UP AT THE BACK
                    #print(i)
                    s[i], s[i+1] = s[i+1], s[i]
                    minSwap += 1

                front += 1
                back -=1

        return minSwap


obj = Solution()
s = 'mamad'
s = 'ntiin'
print(obj.min_swaps(s))


