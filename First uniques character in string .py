from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_counter =  Counter(s)
        index = 0
        for i in s:
            if str_counter[i] ==  1:
                return index
            else:
                index += 1
        return -1

