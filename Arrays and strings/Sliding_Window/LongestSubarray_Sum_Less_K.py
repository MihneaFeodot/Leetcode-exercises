# LENGTH OF WINDOW: RIGHT - LEFT + 1
# TIME Complexity: O(n) because all work that can be done is when right = n and left should increase n times, meaning O(n), or 
# the whole work done inside the loop is amortized O(1) (when something is O(n) the rest can't be O(n))
# SPACE Complexity: O(1) or constant because only 3 variables are used


def find_length(nums: list[int], k: int) -> int :
    left = curr = ans = 0
    
    for right in range(len(nums)) :
        curr += nums[right]
        
        while curr > k :
            curr -= nums[left]
            left += 1
            
        ans = max(ans, right - left + 1)
        
    return ans


if __name__ == '__main__':
    
    print(find_length([3,1,2,7,4,2,1,1,5], 15))