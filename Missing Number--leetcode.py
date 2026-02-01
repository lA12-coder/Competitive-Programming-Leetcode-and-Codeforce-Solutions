from typing import List
class Solution:
    def missingNumber(self, nums):
        num_set = nums
        for i in range(len(nums)+1):
            if i not in num_set:
                return i
        
        
sol = Solution()
res = sol.missingNumber([9,6,4,2,3,5,7,0,1])
print(res)