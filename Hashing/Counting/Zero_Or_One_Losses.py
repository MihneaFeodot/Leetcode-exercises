'''
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

1: 0
2: 0
3: 2
6: 2
7: 1
5: 1
8: 1
4: 1
9: 2
'''


from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losers = defaultdict(int)

        zero_losses = list()
        one_loss = list()

        for winner, loser in matches:
            if winner not in losers:
                losers[winner] = 0
            losers[loser] += 1

        for key, value in losers.items():
            if value == 0:
                zero_losses.append(key)
            elif value == 1:
                one_loss.append(key)

        zero_losses.sort()
        one_loss.sort()
        print([zero_losses, one_loss])
            
sol = Solution()

print(sol.findWinners([[2,3],[1,3],[5,4],[6,4]]))