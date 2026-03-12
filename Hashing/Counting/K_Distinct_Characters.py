# SLIDING WINDOW TYPE OF PROBLEM

'''
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
'''
#TIME Complexity: O(n), the while loop is amortized O(1)
# SPACE Complexity: O(k), the space allocated for the dict is equal to the number of distinct characters allowed

from collections import defaultdict

def find_longest_substring(s: str, k: int) -> int:
    counts = defaultdict(int)

    left = ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1

        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]

            left += 1

        ans = max(ans, right - left + 1)

    return ans

print(find_longest_substring("eceba", 1))
