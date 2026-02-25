import math
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range (math.ceil(len(s)/2)) :
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp