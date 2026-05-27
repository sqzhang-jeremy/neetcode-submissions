# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         # hash->sorting->return k keys
#         # hash

#         # hash_num = {}
#         # for num in nums:
#         #     hash_num[num] = hash_num.get(num, 0) + 1
#         hash_num = Counter(nums)



#         # sorting
#         sort_hash_num = sorted(hash_num.items(), key=lambda item: item[1], reverse=True)
        
#         # return k keys
#         # output = []

#         # for i in range(k):
#         #     output.append(sort_hash_num[i][0])
#         # return output

#         return [num for num, count in sort_hash_num[:k]]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequencies->sort by frequency->take the top k

        # create a hash map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # build a list of [frequency, number] paris from the map

        arr = []

        for (number, frequency) in count.items():
            arr.append([frequency, number])

        arr.sort()

        # take the top k
        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res

