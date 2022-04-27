class Solution(object):
    def minDeletions(self, s):
        freq_count = {}
        for i in s:
            if i in freq_count:
                freq_count[i] += 1
            else:
                freq_count[i] = 1
        freq = list(freq_count.values())
        uniq = set()
        count = 0
        for num in freq:
            while num in uniq and num != 0:
                num -= 1
                count += 1
            uniq.add(num)
        return count


obj = Solution()
obj.minDeletions('ceabaacb')