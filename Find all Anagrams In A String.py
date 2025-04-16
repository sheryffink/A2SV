from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        w = len(s)
        ans = []
        counts = Counter(s)
        countp = Counter(p)
        for i in range(w-n+1):
            r = i+n
        # for let,num in countp.items():
            check = Counter(s[i:r])
            if countp == check:
                ans.append(i)
        return ans


            

        

        
