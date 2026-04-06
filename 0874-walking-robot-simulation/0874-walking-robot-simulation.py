class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        o = set()
        for x, y in obstacles:
            o.add((x, y))

        pos = (0, 0)
        dir = (0, -1)

        cx, cy = 0, 0
        dx, dy = 0, -1

        furthest = 0

        for command in commands:
            if command == -1:
                if dx == 0 and dy == -1:
                    dx, dy = 1, 0
                elif dx == 1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == 0 and dy == 1:
                    dx, dy = -1, 0
                elif dx == -1 and dy == 0:
                    dx, dy = 0,  -1

            elif command == -2:
                if dx == 0 and dy == -1:
                    dx, dy = -1, 0
                elif dx == 1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == 0 and dy == 1:
                    dx, dy = 1, 0
                elif dx == -1 and dy == 0:
                    dx, dy = 0,  1

            else:
                for i in range(command):
                    nx, ny = cx + dx, cy + dy
                    if (nx, -ny) not in o:
                        cx, cy = nx, ny

                furthest = max(furthest, (cx**2 + cy**2))


        return furthest



        


        