"""
Problem Description: Given a string replace the largest repeated substring at every point with an asterisk(*). The goal is end result should be a minimal length string after compression

For example, s = "abcabcd" should become "abc*d", Reason: we know abc has repeated twice, so replace the entire second instance of abc with an *.

and if s = "aabbaabb" it should become "a*bb*", Reason: At index 1, a is repeated twice so put an * there, and aabb has repeated twice so replace it's second instance with an *. In this example we don't put an * right after b at index 3 because aab* would represent aabaab, but that isn't the case.

Solution: The solution I came up with was at every even index check if the first half is equal to the second half, if it is, replace the entire second half with an *.


"""

def compressString(s):
    temp = ""
    i = 0
    while i < len(s):
        if s[:i+1] == s[i+1:2*i+2]:
            temp += s[i] + '*'
            i += (i+2)
        else:
            temp += s[i]
            i += 1
    return temp


s = "abcabcd"
print(compressString(s))
