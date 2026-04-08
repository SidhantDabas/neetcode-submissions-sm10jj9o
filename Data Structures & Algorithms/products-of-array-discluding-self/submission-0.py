class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev_list = []
        suff_list = []
        prev = 1
        suff = 1
        for i in range(len(nums)):            
            if i == 0:
                prev = 1
                suff = 1
            else : 
                prev = prev*nums[i-1]
                suff = suff*nums[len(nums) - i]

            prev_list.append(prev)               
            suff_list.insert(0,suff)
        res = [a * b for a, b in zip(prev_list, suff_list)]
        return res





