from collections import defaultdict
'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

dict = {
    "aet": ["eat", "tea", "ate"],
    "abt": 
}

set = ("aet", "abt", "atn")
'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pairs = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word))
            pairs[word_sorted].append(word)

        return list(pairs.values())
    
sol = Solution()

print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
            