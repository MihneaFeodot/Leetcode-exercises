# TIME Complexity: O(n+n-1) = O(n)
# SPACE Complexity: O(n)
def split_array(nums: list[int]) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = 0

    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]

        if left_section >= right_section:
            ans += 1
    
    return ans

# SAAAAAAAAAAAAAAAAAAAAAAAU 
# Varianta cu SPACE Complexity: O(1)

def split_array_efficient(nums: list[int]) -> int:
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section

        if left_section >= right_section:
            ans += 1

    return ans


if __name__ == '__main__':
    print(split_array([10, 4, -8, 7]))
    print(split_array_efficient([10, 4, -8, 7]))

