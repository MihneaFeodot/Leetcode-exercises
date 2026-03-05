'''
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

two pointers: i and j, both start at index 0 of their respective array

3 cases: i == j, i < j, i > j
i == j: if ans == -1: ans = i (we only need the first element that is common to both arrays, because both arrays are sorted in non-decreasing order and only contain positive values)
i < j: i += 1
i > j: j += 1
'''

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i = j = 0
        ans = -1

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                ans = nums1[i]
                return ans
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

if __name__ == '__main__':

    sol = Solution()

    print(sol.getCommon([1, 2, 3, 6], [1, 3, 4, 5]))