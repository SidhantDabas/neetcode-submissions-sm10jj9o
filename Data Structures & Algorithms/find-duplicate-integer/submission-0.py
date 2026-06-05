class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = set()
        for i in nums:
            if i not in duplicate:
                duplicate.add(i)
            else:
                return i