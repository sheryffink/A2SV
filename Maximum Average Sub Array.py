class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n < 2:
            return nums[0]
        curr_sum = sum(nums[:k])
        avg = curr_sum/k
        maxi = avg
        for i in range(n-k):
            r = i + k
            curr_sum -= nums[i]
            curr_sum += nums[r]
            new_avg = curr_sum/k
            if new_avg > avg:
                avg = new_avg

        return avg

            
        
