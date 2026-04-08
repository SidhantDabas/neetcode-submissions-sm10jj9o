class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s_num = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in s_num:
                return [s_num[diff]+1, i + 1] 
            else:
                s_num[numbers[i]] = i
        return []
            
            
        

