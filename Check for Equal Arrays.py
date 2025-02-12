from collections import Counter
class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        countA = Counter(a)
        countB = Counter(b)
        while countA == countB:
            return True if countA == countB else False
