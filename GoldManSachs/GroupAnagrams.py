"""
Leetcode 49: Group Anagrams
"""
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        sortedStrs = collections.defaultdict(list)
        for word in strs:
            sortWord = sorted(word)
            sortedStrs[tuple(sortWord)].append(word)
        #print(sortedStrs)
        return sortedStrs.values()