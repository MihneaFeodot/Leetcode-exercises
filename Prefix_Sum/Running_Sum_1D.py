class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        return prefix
    
if __name__ == '__main__':
    sol = Solution()
    
    print(sol.runningSum([1, 2, 3, 4]))