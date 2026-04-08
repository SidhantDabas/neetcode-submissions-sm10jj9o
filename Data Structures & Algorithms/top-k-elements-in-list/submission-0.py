class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_table = {}
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        print(counts)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # Start at the end, go to 1
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:  # Stop once we have k elements
                    return result
            