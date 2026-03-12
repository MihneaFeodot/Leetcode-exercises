'''
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        seen = set(sentence)
        
        if len(seen) == 26:
            return True
        else:
            return False
    
sol = Solution()

print(sol.checkIfPangram("thequickbrownfoxjumpsothelazydog"))