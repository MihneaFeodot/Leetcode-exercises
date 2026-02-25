# TIME Complexity: O(n)
# SPACE Complexity: O(1) constant

'''
Example 4: Given an integer array nums and an integer k, 
find the sum of the subarray with the largest sum whose length is k.

k = 4
[3, -1, 4, 12, -8, 5, 6]

'''

def find_best_subarray(nums: list[int], k: int) -> int:
    curr = 0
    
    for i in range(k):
        curr += nums[i]
        
    ans = curr

    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]  
        ans = max(curr, ans)
        
    return ans

if __name__ == '__main__':
    
    print(find_best_subarray([3, -1, 4, 12, -8, 5, 6], 4))  

    