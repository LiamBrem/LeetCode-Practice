class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            time = (target - p) / s
            
            if not stack:
                stack.append(time)
                
            if stack[-1] < time:
                stack.append(time)


        return len(stack)