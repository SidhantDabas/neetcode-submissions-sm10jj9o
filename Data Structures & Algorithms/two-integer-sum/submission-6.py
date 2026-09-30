class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for j in range(len(nums)):
            if target - nums[j] in sums:
                return [sums[target - nums[j]], j]
            else:
                sums[nums[j]] = j
        return []