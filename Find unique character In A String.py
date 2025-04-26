class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for num, dup in counts.items():
                if dup == 1:
                    return s.index(num)
        return -1

        
