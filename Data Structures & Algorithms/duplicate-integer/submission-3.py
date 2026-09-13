class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_dup = set()
        for i in nums:
            if i in list_dup:
                return True
            else:
                list_dup.add(i)
        return False