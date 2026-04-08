class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s_num = {}
        for i in range(len(numbers)):
            if target - numbers[i] in s_num:
                return [s_num[target - numbers[i]]+1, i + 1] 
            else:
                s_num[numbers[i]] = i
        return []
            
            
        

