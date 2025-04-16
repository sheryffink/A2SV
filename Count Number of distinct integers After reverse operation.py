class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        copy_nums = nums.copy()
        for num in nums:
            reverse = int(str(num)[::-1])
            copy_nums.append(reverse)
        distinct_count = len(set(copy_nums))
        return distinct_count
        
