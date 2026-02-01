from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dict.keys():
                return [dict[x],i]
            else:
                dict[nums[i]] = i  
