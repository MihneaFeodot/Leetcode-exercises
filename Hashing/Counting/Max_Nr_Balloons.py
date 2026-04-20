'''
Input: text = "loonbalxballpoon"
Output: 2

Input: text = "nlaebolko"
Output: 1

n: 1
l: 2
a: 1
e: 1
b: 1
o: 2
k: 1


balloon => b: 1, a: 1, l: 2, o: 2, n: 1
'''

from collections import defaultdict
import math
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        appeareances = defaultdict(int)
        balloon = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }
        for c in text:
            appeareances[c] += 1
            
        max = math.inf
        
        for char in balloon:
            max = min(max, appeareances[char] // balloon[char])
            
        return max


sol = Solution()

print(sol.maxNumberOfBalloons("nlaebolkn"))

        
