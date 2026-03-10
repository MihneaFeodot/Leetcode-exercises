# TIME Complexity: O(n)
# SPACE Complexity: O(n)

def find_numbers(nums):
    ans = []
    nums_set = set(nums)

    for num in nums_set:
        if (num - 1 not in nums_set) and (num + 1 not in nums_set):
            ans.append(num)

    return ans

print(find_numbers([1, 3, 4, 11, 5, 6, 7, 8, 1, 3]))