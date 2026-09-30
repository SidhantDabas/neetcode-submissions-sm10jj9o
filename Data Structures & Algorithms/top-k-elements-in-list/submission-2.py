class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        #This is to get frequency value hash map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #This phase is to put all the frequency and elements into heap but also deleting any extra frequency > k
        for num in count.keys():
            heapq.heappush(heap, (count[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        #This phase is to put all the values in heap into a list
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

            