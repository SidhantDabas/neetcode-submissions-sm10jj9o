class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in target_dict:
                return [target_dict[diff], i]
            else:
                target_dict[val] = i
        return []