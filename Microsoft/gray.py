"""
 89. Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.s
"""

class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        # for n =1 ==> [0,1]
        sequence = [0, 1]
        i = 1
        while i < n:
            i += 1
            temp = sequence
            # each value from reverse is added by 2 pow(i-1) where i is the n
            increment_value = 2 ** (i - 1)
            for idx in range(len(temp) - 1, -1, -1):
                sequence.append(temp[idx] + increment_value)

        return sequence