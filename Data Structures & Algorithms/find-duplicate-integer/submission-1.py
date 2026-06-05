class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        for i in nums:
            if i == n:
                return i
            else:
                n = i