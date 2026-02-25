## Time Complexity O(n) (de fapt e O(n+m) dar in Big O pot alege cum vreau eu variabilele)
## Space Complexity O(1) (daca nu luam in considerare output ul ca extra space)

def combine(arr1: list[int], arr2: list[int]) -> list[int] :
    ans = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2) :
        if arr1[i] < arr2[j] :
            ans.append(arr1[i])
            i += 1
            
        else :
            ans.append(arr2[j])
            j += 1
            
    while i < len(arr1) :
        ans.append(arr1[i])
        i += 1
        
    while j < len(arr2) :
        ans.append(arr2[j])
        j += 1
        
    return ans
        
if __name__ == '__main__' :
    
    print(combine([1, 2, 3, 4], [3, 6, 8, 9, 10, 15]))