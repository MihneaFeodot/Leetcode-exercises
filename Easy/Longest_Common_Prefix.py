'''
Input: strs = ["flower","flow","flight"]
Output: "fl"

str1 = strs[1]
str2 = strs[2]

if str1[0] == str2[0]
    ans.append(str1[0])
else return ""


prefix_list = ["flow", ""]
ans = "fl"

i = 1 => str1[1] and str2[1], len(str1) = 4, len(str2) = 6

j = 2



'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        ok = True
        prefix_list = []

        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs) - 1):
            str1 = strs[i]
            str2 = strs[i + 1]

            if not str1 or not str2:
                return ""
            print("S-a trecut")
            ans = ""

            j = 0
            while j < len(str1) and j < len(str2):
                if str1[j] == str2[j]:
                    ans += str1[j]
                else:
                    j = len(str1)
                j += 1
            
            prefix_list.append(ans)

        if prefix_list:
            min_prefix = min(prefix_list)
        for word in prefix_list:
            if word.startswith(min_prefix) == False:
                ok = False
        
        if ok == True and prefix_list:
            return(min_prefix)
        else:
            return ""



sol = Solution()

print(sol.longestCommonPrefix([""]))