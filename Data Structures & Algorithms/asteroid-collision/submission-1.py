class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for aster in asteroids:

            while stack and aster < 0 and stack [-1] > 0:
                diff = aster + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    aster = 0
                else:
                    aster = 0
                    stack.pop()
            
            if aster:
                stack.append(aster)


        return stack

    # [2,4,-4,-1]
    # [5,5]
    # [-10, 5]
    # [10, -5]
    # [10, 2, -5]
                

            

        