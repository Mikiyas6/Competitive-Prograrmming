class Robot:
    def __init__(self, width: int, height: int):
        self.x, self.y = 0, 0
        self.dx, self.dy = 1, 0
        self.width, self.height = width - 1, height - 1
        
    def step(self, num: int) -> None:
        num %= (self.width + self.height) * 2
        if (self.x, self.y) == (0, 0) and (self.dx, self.dy) == (1, 0):
            self.dx, self.dy = self.dy, -self.dx
        while True:
            next_x = self.x + self.dx * num
            next_y = self.y + self.dy * num
            if next_x < 0:
                self.x = 0
                num = -next_x
            elif next_x > self.width:
                self.x = self.width
                num = next_x - self.width
            elif next_y < 0:
                self.y = 0
                num = -next_y
            elif next_y > self.height:
                self.y = self.height
                num = next_y - self.height
            else:
                self.x, self.y = next_x, next_y
                break
            self.dx, self.dy = -self.dy, self.dx

    def getPos(self) -> List[int]:
        return (self.x, self.y)
    
    def getDir(self) -> str:
        return {(0, 1):'North', (1, 0):'East', (0, -1):'South', (-1, 0):'West'}[(self.dx, self.dy)]