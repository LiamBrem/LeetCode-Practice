class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cx = 0
        self.cy = 0
        self.dirs = ["East", "North", "West", "South"]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dir = 0
        self.perimeter = 2 * (self.width + self.height - 2)

    def turn(self):
        self.dir += 1
        self.dir %= 4

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return

        num %= self.perimeter
        if num == 0:
            num = self.perimeter

        while num > 0:
            nx = self.cx + self.directions[self.dir][0]
            ny = self.cy + self.directions[self.dir][1]

            if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                self.dir = (self.dir + 1) % 4
                nx = self.cx + self.directions[self.dir][0]
                ny = self.cy + self.directions[self.dir][1]

            self.cx = nx
            self.cy = ny
            num -= 1
        

    def getPos(self) -> List[int]:
        return [self.cx, self.cy]
        

    def getDir(self) -> str:
        return self.dirs[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()