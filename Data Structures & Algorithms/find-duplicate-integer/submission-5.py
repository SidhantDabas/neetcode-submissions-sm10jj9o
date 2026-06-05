class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n-1
        while low<high:
            mid = low + (high-low)//2
            sumnum = sum(num<=mid for num in nums)

            if sumnum>mid:
                high = mid
            else:
                low = mid+1
        return low