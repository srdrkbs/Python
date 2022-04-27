"""
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
Examples: Input: s = "()"
Output: true
Input: s = "(*))"
Output: true
"""
class Solution(object):
    def checkValidString(self, s):
        closed = []
        star = []
        for idx, char in enumerate(s):
            if char == ')':
                if len(star) == 0 and len(closed) == 0:
                    return False
                if len(closed) != 0:
                    closed.pop()
                    continue
                else:
                    star.pop()
            elif char == '(':
                closed.append(idx)
            else:
                star.append(idx)
        while closed and star:
            if closed[-1] < star[-1]:
                closed.pop()
                star.pop()
            else:
                break
        return len(closed) == 0
