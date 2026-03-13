'''
Example 2: 2248. Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear
in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
'''

# TIME Complexity:
# Let's say there are n arrays each with an average of m elements =>
# => for the first part of the frequency counting it's O(n * m)
# After, in the sorting part where at max m elements are checked, it is O(m * log m)
# SO FINALLY: O(n * m + m * log m) = O(m * (n + log m))

# SPACE Complexity: O(n * m) = the hash map can grow to that size if the arrays all have unique characters intra and inter

from collections import defaultdict

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counts = defaultdict(int)
        
        for arr in nums:
            for x in arr:
                counts[x] += 1
                
        n = len(nums)        
        ans = []
        
        for key in counts:
            print(key)
            if counts[key] == n:
                ans.append(key)
                
        return sorted(ans)
    
sol = Solution()

print(sol.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))