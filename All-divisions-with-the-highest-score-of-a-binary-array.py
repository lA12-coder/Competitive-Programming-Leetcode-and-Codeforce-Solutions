from typing import List
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones_right = nums.count(1)
        zeros_left = 0
        scores = []
        max_value = 0
        for i in range(len(nums)+1):
            score = ones_right + zeros_left
            scores.append(score)
            max_value = max(max_value,score)
            
            if i < len(nums):
                if nums[i] == 0:
                    zeros_left +=1
                else:
                    ones_right -= 1
        
        return [x for x,y in enumerate(scores) if y==max_value]
    

        
    
                
                
                
            
        
        
            
            

        