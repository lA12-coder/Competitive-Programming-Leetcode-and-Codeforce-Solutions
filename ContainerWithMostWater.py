class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height)-1
        while l < r:
            area = (r-l)*min(height[l], height[r])
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area
    
    
sol = Solution()
res = sol.maxArea( height = [1,8,6,2,5,4,8,3,7])
print(res)
