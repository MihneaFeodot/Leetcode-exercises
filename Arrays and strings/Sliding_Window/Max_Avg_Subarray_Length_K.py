# TIME Complexity: O(n)
# SPACE Complexity: O(1), constant
'''
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
'''
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = 0
        
        curr = ans = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)
        
        return ans / k
    
if __name__ == '__main__':
    
    sol = Solution()
    print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))