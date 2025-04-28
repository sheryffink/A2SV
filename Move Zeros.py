class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [k for k in nums if k != 0] + [i for i in nums if i == 0]
        # print(nums)

        
