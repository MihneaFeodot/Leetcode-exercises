'''
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true, because all characters appear twice. 
Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
'''
# TIME Complexity: O(n)
# SPACE Complexity: O(k), where k is the number of characters in the input, 26 is the maxiumum to be precise

from collections import defaultdict, Counter

class Solution:
    def areOccurencesEqual(self, s: str) -> bool:
        # counts = defaultdict(int)
        
        # for c in s:
        #     counts[c] += 1
            
        # frequencies = counts.values()
        
        # return(len(set(frequencies)) == 1)
        
        # this is the simple method, but there is also a ONE-LINER
        
        return(len(set(Counter(s).values())) == 1)
    

sol = Solution()

print (sol.areOccurencesEqual("abacbc"))