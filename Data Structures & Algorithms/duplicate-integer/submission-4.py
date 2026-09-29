class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupli = set()
        for i in nums:
            if i in dupli:
                return True
            else:
                 dupli.add(i)
        return False
