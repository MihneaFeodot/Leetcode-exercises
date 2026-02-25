'''
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

1, ans = 1
1 1, ans = 2
1 1 1, ans = 3
1 1 1 0, ans = 4
1 1 1 0 0, ans = 5
1 1 1 0 0 0, numarul de 0 a depasit limita de 2 (adica k) deci voi scoate de la stanga(incrementez left) pana sunt din nou sub limita
=> 1 1 0 0 0, 1 0 0 0, 0 0 0, 0 0 => ans = 5

0 0 1, ans = 5
0 0 1 1, ans = 5
0 0 1 1 1, ans = 5
0 0 1 1 1 1, ans = 6
0 0 1 1 1 1 0, numarul de 0 a depasit limita de 2 (adica k) deci voi scoate de la stanga(incrementez left) pana sunt din nou sub limita
=> 0 1 1 1 1 0 => ans = 6

Final: ans = 6, lungimea maxima a unui subarray ce contine k maxim de 0 (pt flips) astfel incat sa fie cel mai lung subarray de 1 consecutivi


'''

# TIME Complexity: O(n), amortized O(1) pentru acel while, care este in interiorul for ului, (in teorie ar fi maxim O(2n), dar asta e tot O(n))
# SPACE Complexity: O(1), constant
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        left = curr = ans = 0

        for right in range (len(nums)):
            if nums[right] == 0:
                curr += 1
            
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

if __name__ == '__main__':

    sol = Solution()

    print(sol.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 3))


        
