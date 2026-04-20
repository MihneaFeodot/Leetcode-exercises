'''
Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
'''


from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        appereances = defaultdict(int)
        
        for num in nums:
            appereances[num] += 1
            
        ans = - 1
        
        for num in nums:
            if appereances[num] < 2:
                ans = max(ans, num)
                
        return ans
    
    
sol = Solution()
print(sol.largestUniqueNumber([8,8,9,9]))
                

            