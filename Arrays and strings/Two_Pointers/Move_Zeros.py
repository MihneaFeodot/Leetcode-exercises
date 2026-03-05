'''
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_of_zeros = nums.count(0)

        while number_of_zeros:
            nums.remove(0)
            nums.append(0)
            number_of_zeros -= 1

