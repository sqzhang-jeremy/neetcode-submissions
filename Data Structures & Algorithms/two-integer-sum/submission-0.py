class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_heap = {}

        for i, num in enumerate(nums):
            nums_heap[num] = i


        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_heap and nums_heap[diff] != i:
                return [i, nums_heap[diff]]
        
        return []
            