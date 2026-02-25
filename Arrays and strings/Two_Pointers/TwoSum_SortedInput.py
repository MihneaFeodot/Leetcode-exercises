## Time complexity O(n) (se pot itera maxim de n ori, practic pana cand ajunge unul dintre pointeri la celalalt)
## Space complexity O(1) (nu creste memoria odata cu cresterea marimii datelor de intrare => e constanta complexitatea de spatiu)


def check_for_targets(nums: list[int], target: int) -> bool :
    left = 0
    right = len(nums) - 1
    
    while left < right :
        curr = nums[left] + nums[right]
        if curr == target :
            return True
        
        if curr > target :
            right -= 1
        else :
            left += 1
        
    return False

if __name__ == '__main__' :
    
    print(check_for_targets([1,2,4,6,8,9,14,15], 25))