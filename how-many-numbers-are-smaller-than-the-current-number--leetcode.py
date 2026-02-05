from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0]*(101)
        
        # Create the frequency array
        for v in nums:
            count[v] += 1
        
        # prefix sum
        for i in range(1,len(count)):
            count[i] += count[i-1]
            
        # Build the result 
        for i,num in enumerate(nums):
            if num == 0:
                nums[i] = 0
            else:
                nums[i] = count[num-1]
        return nums   
            
        

print(Solution().smallerNumbersThanCurrent(nums = [8,1,2,2,3])) #output=[4, 0, 1, 1, 3]