'''
Input: nums = [3,0,1]
n = 3 (len(nums))

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

# TIME Complexity: O(n), or actually O(n + n), but that is O(n)
# SPACE Complexity: O(n), because of the declaration of the nums_set
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i
            
        return -1
    

sol = Solution()

print(sol.missingNumber([9, 6, 4, 2, 3, 5, 8, 0, 1]))