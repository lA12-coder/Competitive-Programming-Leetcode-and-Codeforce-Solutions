class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        seeker = 1
        
        while seeker <= len(nums)-1 and holder < seeker:
            if nums[holder] != 0:
                holder+=1
                seeker+=1
            else:
                if nums[seeker]!=0:
                    nums[seeker],nums[holder] = nums[holder],nums[seeker]
                    seeker +=1
                    holder+=1
                else:
                    seeker+=1
