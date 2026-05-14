class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for item in nums:
            if item not in countMap:
                countMap[item] = 1
            else:
                countMap[item] += 1
        # wrong solution
        # for (k,v) in countMap:
        #     if v > 1:
        #         return True

        for (k, v) in countMap.items():
            if v > 1:
                return True
        return False
        