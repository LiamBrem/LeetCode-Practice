class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        rows = len(wall)
        slots = {}

        if rows == 1:
            return 1 if len(wall[0]) == 1 else 0

        for row in range(rows):
            cols = len(wall[row])
            cuts = 0
            for col in range(cols -1):
                cuts += wall[row][col]
                if cuts in slots:
                    slots[cuts] += 1
                else:
                    slots[cuts] = 1

        maxSlots = 0

        for slot in slots:
            if slots[slot] > maxSlots:
                maxSlots = slots[slot]

        return rows - maxSlots
                    


        

                