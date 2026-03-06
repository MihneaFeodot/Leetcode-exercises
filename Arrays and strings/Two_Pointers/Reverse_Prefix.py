# TIME Complexity: O(n), maxim O(n+n) care e tot O(n)
# SPACE Complexity: O(1)

'''
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            end_reverse_index = word.index(ch)
            start_reverse_index = 0
            word_list = list(word)
            
            while start_reverse_index < end_reverse_index:
                tmp = word_list[start_reverse_index]
                word_list[start_reverse_index] = word_list[end_reverse_index]
                word_list[end_reverse_index] = tmp
                
                start_reverse_index += 1
                end_reverse_index -= 1
                
            return "".join(word_list)
        
        
if __name__ == '__main__':
    
    sol = Solution()
    
    print(sol.reversePrefix("abcdefd", "d"))