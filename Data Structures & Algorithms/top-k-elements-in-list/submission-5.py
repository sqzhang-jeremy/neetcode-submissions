# Hash+bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a hash map
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # create a bucket
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq.items():
            buckets[freq].append(num)

        res = []
        for count in range(len(buckets) -1, 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res



