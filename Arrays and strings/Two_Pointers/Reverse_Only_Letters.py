'''
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

left = 0
right = len(s) - 1

First 
'''

def reverseOnlyLetters(s: str) -> str:
    ans = list(s)

    left = 0
    right = len(ans) - 1

    while left < right:
        if not (('A' <= ans[left] <= 'Z') or ('a' <= ans[left] <= 'z')):
            print("Non letter character detected! for LEFT")
            left += 1
            continue

        if not (('A' <= ans[right] <= 'Z') or ('a' <= ans[right] <= 'z')):
            print("Non letter character detected! for right")
            right -= 1
            continue
            
        temp = ans[left]
        ans[left] = ans[right]
        ans[right] = temp
        left += 1
        right -= 1

        
    return "".join(ans)

if __name__ == '__main__':

    

    print(reverseOnlyLetters("a-bC-dEf-ghIj"))

        