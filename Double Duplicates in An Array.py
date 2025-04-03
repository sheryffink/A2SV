from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        duplicates = []
        for num,dup in counts.items():
            if dup == 2:
                duplicates.append(num)
        return duplicates
