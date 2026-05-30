class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                res = [l + 1, r + 1]
                return res
        
        return res


        