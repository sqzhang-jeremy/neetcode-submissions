class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        array = []
         
        for i in range(len(position)):
            array.append((target - position[i], speed[i]))

        print("Before Sort:", array)
        array.sort()
        print("After Sort:", array)

        time = []
        stack = []

        for i in range(len(array)):
            time.append(array[i][0] / array[i][1])


        for val in time:
            if not stack:
                stack.append(val)
    
            if val > stack[-1]:
                stack.append(val)

        
        return len(stack)


        



        