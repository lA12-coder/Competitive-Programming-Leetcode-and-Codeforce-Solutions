from typing import List
class Solution:
    def lastIndexOfNumber(self,lst,value):
        try:
            return len(lst)-1-next(i for i,x in enumerate(reversed(lst)) if value==x)
        except StopIteration:
            return -1
    
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}
        for chr in s:
            if chr not in last_occurence.keys():
                last_occurence[chr]=self.lastIndexOfNumber(list(s),chr)
                
        partitionStart = 0
        partitionEnd = 0
        partitionSize = []
        
        for i in range(len(s)):
            partitionEnd = max(partitionEnd,last_occurence[s[i]])
            if i == partitionEnd:
                partitionSize.append(i-partitionStart+1)
                partitionStart = i+1
                
        return partitionSize
                
                
            
        
 
print(Solution().partitionLabels(s = "ababcbacadefegdehijhklij"))

