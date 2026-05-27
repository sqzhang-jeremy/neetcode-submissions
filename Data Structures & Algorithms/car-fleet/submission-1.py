import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # ensure about the order of these cars
        car = [] #(position, speed)

        for i in range(len(position)):
            car.append([position[i], speed[i]])

        car.sort(reverse=True)

        # calculate the final times

        times = []

        for (pos, spd) in car:
            times.append((target - pos) / spd)

        # create a stack to form car fleets

        stack = []

        for time in times:
            if not stack:
                stack.append(time) 
            elif time > stack[-1]:
                stack.append(time)


        return len(stack)

    

        