'''
Given an array of strings strs, group the anagrams together.

For example, given strs = ["eat","tea","tan","ate","nat","bat"], 
return [["bat"],["nat","tan"],["ate","eat","tea"]].
'''


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())
    
    
sol = Solution()

print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))