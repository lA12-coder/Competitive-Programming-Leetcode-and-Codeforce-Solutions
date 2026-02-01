from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # saved the image dimensions.
        m = len(img)
        n = len(img[0])
        
        # Iterate over the cell of the image
        for row in range(m):
            for col in range(n):
                # Initialize the sum and count
                sum = 0
                count = 0
                
                # Iterate over all plausible nine indices.
                for x in (row-1, row, row+1):
                    for y in (col-1, col, col+1):
                        # If indices form a valid neighbor
                        if 0 <= x < m and 0 <= y < n:
                            # Extract the original value of img[x][y]
                            sum += img[x][y] & 255
                            count += 1
                            
                            
                # Encode the smoothed value in img[row][col]   
                img[row][col] |= (sum//count)<<8
        
        # Extract the smoothed value from encoded img[row][col] 
        for row in range(m):
            for col in range(n):
                img[row][col] >>= 8
                
                
        # return the smoothed image
        return img
    
print(Solution().imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
            