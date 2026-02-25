def is_palindrome(arr: str) -> bool:
    left = 0
    right = len(arr) - 1
     
    while left < right:
        if arr[left] != arr[right]:
            return False
        
        left += 1
        right -= 1
             
    return True


if __name__ == '__main__' :
    
    print(is_palindrome('148410'))

