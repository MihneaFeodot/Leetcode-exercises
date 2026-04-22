'''
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.


dic = {}
        dic[0] = -1
        ans = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in dic:
                ans = max(ans, i - dic[count])
            else:
                dic[count] = i
'''

from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        counts[0] = -1
        ans = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            if count in counts:
                ans = max(ans, i - counts[count])
                print(ans)
            else:
                counts[count] = i
        
        
                
        return ans
    
sol = Solution()

print(sol.findMaxLength([0,1,1,1,1,1,0,0,0]))