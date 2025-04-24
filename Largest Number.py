class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        changed = list(map(str, nums))
        # print(changed)
        changed.sort(key = lambda x: x*10, reverse = True)
        if changed[0] == "0":
            return "0"
        found = "".join(changed)
        return found
        


        
            

            

        


        
        
