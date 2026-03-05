'''
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

left = 6
right = 8

ans = [s[4], s[3], s[2], s[1], s[5], ]
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_str = ''
        for word in words:
            reversed_str += word[::-1] + ' '
        return reversed_str.strip()

if __name__ == '__main__':

    sol = Solution()

    print(sol.reverseWords("Let's take LeetCode contest"))




