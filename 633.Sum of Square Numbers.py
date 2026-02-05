import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max =  math.ceil(math.sqrt(c))
        arr =  range(max+1)
        left = 0
        right = len(arr)-1
        
        while left<right:
            if arr[left]**2 + arr[right]**2==c:
                return True
            else:
                if arr[left]**2 + arr[right]**2<c:
                    left+=1
                elif arr[left]**2 + arr[right]**2>c:
                    right-=1
        else:
            if right==left:
                if 2*arr[right]**2==c:
                    return True

        return False