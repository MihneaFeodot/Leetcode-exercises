from collections import defaultdict
'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

freq = {
    "a": 1,
    "b": 1,
    "c": 1
}
'''

# Time Complexity: O(n), amortized O(1) inside while
# Space Complexity: O(n), the space occupied by the dict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0

        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
    
sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))