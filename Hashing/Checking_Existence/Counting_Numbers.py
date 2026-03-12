'''
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
'''

class Solution:
    def countElements(self, arr: list[int]) -> int:
        arr_set = set(arr)

        ans = 0

        for i in arr:
            if (i+1) in arr_set:
                ans += 1
        
        return ans
    
sol = Solution()

print(sol.countElements([1, 1, 2]))