class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        lef = 0
        new_ans = []
        right = nums.count(1)
        ans.append(right)
        for i in range(n):
            if nums[i] == 0:
                lef +=1
            elif nums[i] == 1:
                right -= 1
            ans.append(right+lef)

        maxi = max(ans)
        for j in range(len(ans)):
            if ans[j] == maxi:
                new_ans.append(j)



        return new_ans

                


       
                


        
