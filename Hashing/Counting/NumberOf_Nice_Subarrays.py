'''
Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1, 1], k = 3, the answer is 2. 
The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].

ans = 4
curr = 5

counts = {
    0: 1
    1: 1
    2: 2
    3: 1
    4: 1
    5: 1
}
'''
# TIME Complexity: O(n), only an iteration thorugh nums, which is of n length
# SPACE Complexity: O(n), the dict length increases every time n increases

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            
            ans += counts[curr - k]
            
            counts[curr] += 1
            
        return ans
    
sol = Solution()

print(sol.numberOfSubarrays([1, 1, 2, 1, 1, 1], 3))