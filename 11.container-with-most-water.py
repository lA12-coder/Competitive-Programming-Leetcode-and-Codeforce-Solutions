class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max = 0
        
        while left <  right:
            if height[left]==height[right]:
                area = height[left]*(right-left)
                left+=1

            else:
                min_height = min(height[left],height[right])
                area = min_height *(right-left)
                if height[left]==min_height:
                    left+=1
                if height[right]==min_height:
                    right-=1
                    
            if max < area:
                max = area
        return max