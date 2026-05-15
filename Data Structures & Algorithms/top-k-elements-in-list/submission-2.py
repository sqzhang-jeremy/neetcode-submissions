class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hash->sorting->return k keys
        # hash

        hash_num = {}
        for num in nums:
            hash_num[num] = hash_num.get(num, 0) + 1


        # sorting
        sort_hash_num = sorted(hash_num.items(), key=lambda item: item[1], reverse=True)
        # return k keys

        output = []

        for i in range(k):
            output.append(sort_hash_num[i][0])


        return output