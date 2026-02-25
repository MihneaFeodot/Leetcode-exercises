'''
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. 
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
'''

# TIME Complexity: O(n + m), unde m = lungimea listei cu numere, len(queries) (daca nu faceam cu prefix sum, ar fi fost O(n*m), pt ca trb parcurs vectorul de fiecare data pentru fiecare querie)
# SPACE Complexity: O(n), folosesc n spatiu ca sa creez lista cu sume, n = len(nums)
def answer_queries(nums: list[int], queries: list[list[int]], limit: int) -> list[int]:
    prefix = [nums[0]]

    for i in range (1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []

    for x, y, in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)
    
    return ans

if __name__ == '__main__':

    print(answer_queries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))

    
