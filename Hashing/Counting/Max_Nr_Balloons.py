'''
Input: text = "loonbalxballpoon"
Output: 2

Input: text = "nlaebolko"
Output: 1


balloon => b: 1, a: 1, l: 2, o: 2, n: 1
'''

from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        appeareances = defaultdict()
        
        for c in text:
            appeareances[c] += 1
            
        ans = 0
        
     
                   
        
