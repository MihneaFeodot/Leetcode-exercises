# TIME Complexity: O(n), because the search operation in a set is only O(1)
# SPACE Complexity: O(n), the size of the set increases linearly ### Actually, this is only O(1) as there are a maximum of 26 characters in the English alphabet

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for c in s:
            if c in seen:
                return c
            
            seen.add(c)


sol = Solution()

print(sol.repeatedCharacter("maea"))