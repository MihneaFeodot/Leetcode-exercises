'''
Example 4: 560. Subarray Sum Equals K

Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

Let's walk through an example to see why the algorithm described above works for this problem. 
Let's say we have nums = [1, 2, 1, 2, 1], k = 3. There are four subarrays with sum 3 - [1, 2] twice and [2, 1] twice.

The prefix sum for this input, which is what curr represents during iteration, is [0, 1, 3, 4, 6, 7]. 
You can see that there are three differences in this array of 3:   (4 - 1), (6 - 3), (7 - 4).

But we said that there are four valid subarrays? Recall that we need to initialize our hash map with 0: 1, 
considering the empty prefix. This is because if there is a prefix with a sum equal to k, then without initializing 0: 1, 
curr - k = 0 wouldn't show up in the hash map and we would "lose" this valid subarray.

So at indices 1, 2, 3, and 4, we find curr - k has been seen prior. 
The elements are all positive so each value of curr - k only showed up once, and hence our answer is 4.

nums = [1, 2, 1, 2, 1], k = 3

counts = {
    0: 1
    1: 1
    3: 1
    4: 1
    6: 1
    7: 1
}

ans = 4

curr = 7
'''
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        
        # VERY IMPORTANT, the first prefix sum is 0 because the prefix sum is empty initially
        
        counts[0] = 1
        
        ans = curr = 0
        
        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
            
        return ans
    
sol = Solution()

print(sol.subarraySum([1, 2, 1, 2, 1], 3))