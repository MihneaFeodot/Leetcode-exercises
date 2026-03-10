# TIME Complexity: O(n), because of the iteration overy every item, but then the search is only O(1), because of the hash map or dictionary
# SPACE Complexity: O(n), the space increases linearly every time the size of n is increased, as the length of the dictionary increseases every time


class Solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in dic: # This operation is O(1) !!!
                return [i, dic[complement]]

            dic[num] = i

sol = Solution()
print(sol.TwoSum([2, 9, 4, 5, 6], 8))


