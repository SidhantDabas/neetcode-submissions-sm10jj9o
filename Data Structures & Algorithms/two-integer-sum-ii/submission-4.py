class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l<r:
            estimate = numbers[l] + numbers[r]
            if estimate > target:
                r -= 1
            if estimate < target:
                l += 1
            if estimate == target:
                return [l+1,r+1]
        return []
            
        

