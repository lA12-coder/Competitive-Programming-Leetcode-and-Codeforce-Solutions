from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = Counter(s)
        t_freq = Counter(t)
        count = 0
        for w in t_freq:
            if t_freq[w] > s_freq[w]:
                count += (t_freq[w]-s_freq[w])
                
        return count
    
