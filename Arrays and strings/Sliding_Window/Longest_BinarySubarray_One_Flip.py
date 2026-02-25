# LENGTH WINDOW: RIGHT - LEFT + 1
# TIME Complexity: O(n) because the while inside the loop is an amortized O(1)
# SPACE Complexity: O(1) or constant, because the integers are only 3 
def find_length(s: str) -> int:
    left = curr = ans = 0
    
    for right in range(len(s)):
        
        if s[right] == "0":
            curr += 1
        
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
            
        ans = max(ans, right - left + 1)
        
        
    return ans

if __name__ == '__main__':
    print(find_length("011101100110"))
        