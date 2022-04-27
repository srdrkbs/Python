"""
Leetcode 443: StringCompression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

"""

class Solution:
    def compress(self, chars):
        N = len(chars)
        if N > 1:
            temp = chars[0]
        else: return len(chars)
        count = 1  #count of characters
        compres = ""  #appending charracter and their count
        i = 1
        while i < N:
            if chars[i] == temp:  # if temp is equal to its next character then increment count
                count += 1
            if chars[i] != temp:   # concatenting the character and their count to the compres
                compres = compres + chars[i-1]
                if 1 < count :  # if count greater than one appending the count as string to the compress
                    compres = compres + str(count)
                temp = chars[i]  # updating temp with new character
                count = 1  # updating the count or restarting the count
            i += 1
        if i == N :  # appending the last character and its count to the compress
            compres = compres + chars[i - 1]
            if 1 < count:
                compres = compres + str(count)

        chars[:] = list(compres)  # updating the char with the new compres string
        print(chars)
        return len(chars)


obj = Solution()
chars = ["a","a","b","b","c","c","c"]
#chars = ["a","a","a","b","b","a","a"]
#chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#chars = ["a","b","c"]
print(obj.compress(chars))




