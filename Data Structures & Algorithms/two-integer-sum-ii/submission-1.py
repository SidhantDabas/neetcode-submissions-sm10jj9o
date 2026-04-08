class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1, len(numbers)):
            j = i-1
            print(i,j)
            diff = target - numbers[i]
            while j != -1:
                print("i:", numbers[i] ,"Value", numbers[j], "Diff", diff)

                if diff == numbers[j]:
                    return [j+1,i+1] 
                
                j -= 1
        return []
            
            
        

