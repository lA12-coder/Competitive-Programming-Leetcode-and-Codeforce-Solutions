from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        
        while read < len(chars):
            current_char = chars[read]
            count = 0
            
            while read<len(chars) and current_char == chars[read]:
                read+=1
                count +=1
                
            chars[write] = current_char
            write+=1
            
            if count > 1:
                count = list(str(count))
                for num in count:
                    chars[write] = num
                    write+=1
        
        return write
    
    
sol = Solution()
print(sol.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
            