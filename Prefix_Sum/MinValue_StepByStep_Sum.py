'''
[-3,2,-3,4,2]

[-3,-1,-4,0,2]

sV = 1
[-2] => sV = 2 , [-1] => sV = 3, [0] => sV = 4
'''

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        startValue = 1
        i = 0
        while i < len(nums):
            sum = startValue + prefix[i]

            if sum < 1:
                startValue += 1
                i -= 1
            i += 1
                
        return startValue