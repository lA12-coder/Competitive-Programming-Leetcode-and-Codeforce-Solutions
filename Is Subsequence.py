class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        l = 0
        r = 0
        if s == '':
            return True
        while r<len(t):
            if t[r] != s[l]:
                r+=1
            else:
                counter +=1
                r+=1
                l+=1
                
        if counter != len(s):
            return False
        return True
    
sol = Solution()
res = sol.isSubsequence(s = "", t = "ahbgdc")
print(res)