class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 1

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            
        for num in seen:
            if num - 1 not in seen:  
                    i = 1
                    # while True:
                    #     if num + i in seen:
                    #         longest = i + 1
                    #         i += 1
                    #     else:
                    #         break
                    while num + i in seen:
                        longest = max(longest, i + 1)
                        i += 1 
                    


        return longest if nums else 0



                


        




